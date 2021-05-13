N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]

ans = 10 ** 10

# 4bit search
for i in range(4**N):
    mask = i
    NowCost = 0
    Group0 = []
    Group1 = []
    Group2 = []
    NonGroup = []
    for j in range(N-1, -1, -1):
        if mask % 4 == 0:
            Group0.append(L[j])
            mask //= 4
        elif mask % 4 == 1:
            Group1.append(L[j])
            mask //= 4
        elif mask % 4 == 2:
            Group2.append(L[j])
            mask //= 4
        else:
            NonGroup.append(L[j])
            mask //= 4
    if len(Group0) == 0 or len(Group1) == 0 or len(Group2) == 0:
        continue
    NowCost += 10 * (len(Group0) - 1)
    LengthGroup0 = sum(Group0)
    NowCost += 10 * (len(Group1) - 1)
    LengthGroup1 = sum(Group1)
    NowCost += 10 * (len(Group2) - 1)
    LengthGroup2 = sum(Group2)
    NowCost += abs(A - LengthGroup0)
    NowCost += abs(B - LengthGroup1)
    NowCost += abs(C - LengthGroup2)
    ans = min(ans, NowCost)
print(ans)

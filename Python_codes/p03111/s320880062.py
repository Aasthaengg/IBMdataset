# ABC119C
# Synthetic Kadomatsu
Enter = list(map(int, input().split()))
N = Enter[0]
L = [int(input()) for _ in range(N)]

ans = 10 ** 10

# 4 bist search
for i in range(4**N):
    mask = i
    NowCost = 0
    Group = [[] * 4 for _ in range(4)]
    for j in range(N-1, -1, -1):
        Group[mask%4].append(L[j])
        mask //= 4
    if len(Group[0]) == 0 or len(Group[1]) == 0 or len(Group[2]) == 0:
        continue
    for j in range(3):
        NowCost += 10 * (len(Group[j]) - 1)
        NowCost += abs(sum(Group[j]) - Enter[j+1])
    ans = min(ans, NowCost)
print(ans)

N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

ans = 0
for a in A:
    allsum = C
    for x, y in zip(a, B):
        allsum += x*y
    if allsum > 0:
        ans += 1

print(ans)
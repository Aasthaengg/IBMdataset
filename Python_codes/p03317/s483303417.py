N, K = map(int, input().split())
Ax = list(map(int, input().split()))
if N == K:
    print(1)
    exit()

N -= K
ans = 1

while N > 0:
    N = N-(K-1)
    ans += 1

print(ans)

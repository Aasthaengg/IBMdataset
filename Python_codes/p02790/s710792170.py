N, M = list(map(str, input().split()))

n = N
for i in range(1, int(M)):
    n += N

m = M
for i in range(1, int(N)):
    m += M

ans = [n, m]
ans.sort()

print(ans[0])
N, L = map(int,input().split())

apples = [L+i for i in range(N)]
total = sum(apples)

min_d, ans = 10**9, 0
for i in range(N):
    d = abs(apples[i])
    if d < min_d:
        min_d = d
        ans = total - apples[i]

print(ans)
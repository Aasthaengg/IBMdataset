N = int(input())
vs = list(map(int, input().split()))
cs = list(map(int, input().split()))

ans = 0
for i in range(N):
    diff = vs[i]-cs[i]
    if diff > 0:
        ans += diff


print(ans)

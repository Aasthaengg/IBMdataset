N, L = map(int, input().split())
ans = 0
for i in range(N):
    ans += i+L
if L < 0 and N+L-1 < 0:
    ans -= N+L-1
elif L > 0 and N+L-1 > 0:
    ans -= L
print(ans)

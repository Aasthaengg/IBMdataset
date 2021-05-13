N, K = map(int, input().split())
x = list(map(int, input().split()))

ans = float("inf")

for i in range(N-K+1):
    lef = x[i]
    rig = x[i+K-1]
    ans = min(ans, abs(lef)+abs(rig-lef), abs(rig)+abs(rig-lef))
print(ans)

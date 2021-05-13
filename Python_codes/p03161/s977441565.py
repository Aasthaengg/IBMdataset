N, K = map(int, input().split())
h = list(map(int, input().split()))
 
DP = [0]
for i in range(N-1):
    act = float("inf")
    for k in range(K):
        if i-k < 0 : continue
        act = min(DP[-1-k] + abs(h[i-k]-h[i+1]) , act)
    DP += [act]
 
print(DP[-1])

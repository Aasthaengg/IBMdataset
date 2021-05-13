H,N = map(int,input().split())
Alist = []
Blist = []
for _ in range(N):
    A,B = map(int,input().split())
    Alist.append(A)
    Blist.append(B)

dp = [float('inf')]*(H+1)
dp[0] = 0
for h in range(H+1):
    for n in range(N):
        damage = Alist[n]
        cost = Blist[n]
        first_index = min(h + damage, H)
        dp[first_index] = min(dp[h] + cost, dp[first_index])
        
print(dp[-1])
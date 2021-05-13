n,k = map(int,input().split())
MOD = 998244353
hani = []
for _ in range(k):
    l,r = map(int,input().split())
    hani.append((l,r))

rui = [0] * (n+1)
cur = [0] * n
rui[1] = 1
cur[0] = 1

for i in range(1,n):
    for j in range(k):
        left = max(0,i-hani[j][0]+1)
        right = max(0,i-hani[j][1])
        
        cur[i] = (cur[i] + MOD + rui[left] - rui[right]) % MOD
        
    rui[i+1] = (rui[i] + cur[i]) % MOD
    
print(cur[n-1])
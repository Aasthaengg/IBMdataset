
n, m = map(int, input().split())
ab = []
c= []
keys = ["" for _ in range(m)]

for i in range(m):
    ab.append(list(map(int, input().split())))
    kari = list(map(int, input().split()))
    c.append(kari)
    for j in range(n):
        if j+1 in kari:
            keys[i] = keys[i]+"1"
        else:
            keys[i] = keys[i] + "0"

all_patterns = ["0","1"]
options = ["0", "1"]

for _ in range(n-1):
    all_patterns = [j+i for i in (options) for j in all_patterns]

dp = [1e+10 for i in range(2**n)]
dp[0] = 0

#%%
for j in range(m):
    for i in range(len(dp)):
        kari1 = dp[i]+ab[j][0]
        kari2 = dp[i|int(keys[j],2)]
        if kari1 < kari2:
            dp[i|int(keys[j],2)] = kari1

if dp[-1] != 1e+10:
    print(dp[-1])
else:
    print(-1)
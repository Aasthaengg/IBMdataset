n,m = map(int, input().split())
root = {}

for i in range(m):
    c,d = map(int, input().split())
    if c not in root:
        root[c] = []
    if d not in root:
        root[d] = []
    root[c].append(d)
    root[d].append(c)
sirusi = [0] *(n+1)
dp = [2*m] * (n+1)
dp[1]=0
before = [1]
while True:
    tmp=[]
    flag=0
    for b in before:
        for r in root[b]:
            if dp[r] > dp[b] +1:
                dp[r] = dp[b] +1
                sirusi[r] = b
                flag += 1
                tmp.append(r)
    before = tmp
    if flag == 0:
        break

if sirusi.count(0)>2:
    print("No")
    exit()

print("Yes")
for i in range(2,n+1):
    print(sirusi[i])
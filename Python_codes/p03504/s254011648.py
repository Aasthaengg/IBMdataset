
N,C = map(int,input().split())
s = [0]*N
t = [0]*N
c = [0]*N
for i in range(N):
    s[i],t[i],c[i] = map(int,input().split())
    c[i] -= 1
    
rec = [[0]*(30) for _ in range(10**5+1)]
for i in range(N):
    rec[t[i]][c[i]] -= 1
    
for i in range(N):
    if rec[s[i]][c[i]] != 0:
        rec[s[i]][c[i]] += 1                
    else:
        rec[s[i]-1][c[i]] += 1

simu = [[0]*(30) for _ in range(10**5+1)]
tmp = 0
for j in range(30):
    simu[0][j] += rec[0][j]
    tmp += simu[i][j]
ans = tmp
for i in range(1,10**5+1):
    tmp = 0
    for j in range(30):
        simu[i][j] += simu[i-1][j] + rec[i][j]
        tmp += simu[i][j]
    ans = max(ans,tmp)
print(ans)

    
    

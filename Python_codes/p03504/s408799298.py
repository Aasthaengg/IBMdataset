N,C = map(int,input().split())

data = [[0]*(10**5+1) for i in range(C)]

for i in range(N):
    s,t,c = map(int,input().split())
    c -= 1
    for i in range(s,t+1):
        data[c][i] = 1

ans = 0

for i in range(1,10**5+1):
    count = 0
    for j in range(C):
        count += data[j][i]
    ans = max(ans,count) 

print(ans)
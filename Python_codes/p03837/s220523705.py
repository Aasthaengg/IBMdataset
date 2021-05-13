N,M=map(int,input().split())
h=[list(map(int, input().split())) for i in range(M)]
s=[[10**6]*N for i in range(N)]
for i in h:
    s[i[0]-1][i[1]-1]=i[2]
    s[i[1]-1][i[0]-1]=i[2]
for i in range(N):
    for j in range(N):
        for k in range(N):
            s[j][k] = min(s[j][k],s[j][i] + s[i][k])
a=0
for i in h:
    if s[i[0]-1][i[1]-1]!=i[2]:
        a+=1
print(a)
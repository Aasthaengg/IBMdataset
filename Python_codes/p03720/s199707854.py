n,m=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(m)]
c=[0]*n
for i in range(m):
    c[ab[i][0]-1]+=1
    c[ab[i][1]-1]+=1
for i in range(n):
    print(c[i])
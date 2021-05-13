n,m=map(int,input().split())
d={}
for i in range(n):
    d[i]=0
for i in range(m):
    a,b=map(int,input().split())
    d[a-1]+=1
    d[b-1]+=1
for i in range(n):
    print(d[i])
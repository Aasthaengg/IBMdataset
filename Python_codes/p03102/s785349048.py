n,m,c=map(int,input().split())
l=list(map(int,input().split()))
h=0
for i in range(n):
    d=list(map(int,input().split()))
    s=c
    for i in range(m):
        s+=l[i]*d[i]
    if(s>0):
        h+=1
print(h)

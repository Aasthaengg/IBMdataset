n,t=map(int,input().split())
t1=list(map(int,input().split()))
s=t
k=0
for i in range(1,n):
    if t1[i]-k>=t:
        s=s+t
    else:
        s=s+t1[i]-k
    k=t1[i]
print(s)
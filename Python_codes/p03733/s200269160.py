n,t=map(int,input().split())
l=list(map(int,input().split()))
s=0

for i in range(1,n):
    if l[i]-l[i-1]>=t:
        s+=t
    else:
        s+=(l[i]-l[i-1])
print(s+t)
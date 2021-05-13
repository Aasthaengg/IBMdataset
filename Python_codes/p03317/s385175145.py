n,k=map(int,input().split())
a=list(map(int,input().split()))
num=min(a)
if a[0]==num:
    n-=1
if a[-1]==num:
    n-=1
n-=1
k-=1
print(-1*(n//-k))

n,m=map(int,input().split())
l=list(map(int,input().split()))
s=sum(l)
d=n-s
print(max(-1,d))
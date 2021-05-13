n,m=map(int,input().split())
l=list(map(int,input().split()))
s=sum(l)
if(s>=n):
    print("Yes")
else:
    print("No")
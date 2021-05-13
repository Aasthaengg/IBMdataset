n,m=map(int,input().split())

a=list(map(int,input().split()))
s=sum(a)

print(n-s if n-s>=0 else "-1")

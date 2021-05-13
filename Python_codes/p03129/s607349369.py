n,k=map(int,input().split())
m=n//2 if n%2==0 else n//2+1
print("YES") if k<=m else print("NO")

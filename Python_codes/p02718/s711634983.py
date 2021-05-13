n,m=map(int,input().split())
a=list(map(int,input().split()))
x=0
w=sum(a)
for i in range(n):
    if a[i]*4*m >= w:
        x += 1
print("Yes" if x>=m else "No")
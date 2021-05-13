n=int(input())
a=list(map(int,input().split()))

m=max(a)
r=0
for i in range(n):
    if abs(m/2-a[i])<abs(m/2-r):
        r=a[i]

print(m,r)
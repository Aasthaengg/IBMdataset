n=int(input())
a=list(map(int,input().split()))
p=[0 for i in a]
p[0]=2*sum(a[::2])-sum(a)
for i in range(n-1):
    p[i+1]=2*a[i]-p[i]
print(*p)
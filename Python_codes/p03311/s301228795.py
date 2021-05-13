n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    a[i] -= i + 1
a.sort()
b1 = a[n // 2]
b2 = a[(n // 2 ) - 1]
r1=0
r2=0
for i in range(n):
    r1+=abs(a[i]-b1)
    r2+=abs(a[i]-b2)
print(min(r1,r2))
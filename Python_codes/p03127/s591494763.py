import math
n=int(input())
a=list(map(int,input().split()))
a.sort()
b=a[n-1]
for i in range(n-1):
    b=math.gcd(a[i],b)
print(b)
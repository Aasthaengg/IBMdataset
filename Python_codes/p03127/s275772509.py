import math

n = int(input())
a = list(map(int,input().split()))

tmp = a[0]
for i in range(1,len(a)):
    tmp = math.gcd(tmp,a[i])
print(tmp)
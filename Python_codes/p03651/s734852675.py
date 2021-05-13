import math
n,k = map(int,input().split())
a = list(map(int,input().split()))
if k in a:
    print("POSSIBLE")
    exit()
tmp = a[0]
for i in range(1,n):
    tmp = math.gcd(tmp,a[i])
for i in a:
    if i > k and (i-k) % tmp == 0:
        print("POSSIBLE")
        exit()
print("IMPOSSIBLE")
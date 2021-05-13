import math
n,k = map(int,input().split())
l = list(map(int,input().split()))
if max(l) < k:
    print("IMPOSSIBLE")
    exit()

x = l[0]
for i in l:
    x = math.gcd(x,i)

if k%x:
    print("IMPOSSIBLE")
else:
    print("POSSIBLE")


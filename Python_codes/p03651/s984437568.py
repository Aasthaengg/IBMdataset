import math
n,k = map(int,input().split())
l = sorted(list(map(int,input().split())))
if l[-1] < k:
    print("IMPOSSIBLE")
    exit()
if k in l:
    print("POSSIBLE")
    exit()


x = l[0]
for i in l[1:]:
    x = math.gcd(x,i)

if x == 1:
    print("POSSIBLE")
else:
    for i in l:
        if (k-i)%x == 0:
            print("POSSIBLE")
            exit()
    print("IMPOSSIBLE")


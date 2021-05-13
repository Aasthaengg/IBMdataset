import fractions

n , k = map(int,input().split())
a = list(map(int,input().split()))
if max(a) < k:
    print("IMPOSSIBLE")
    exit()
f = a[0]
for i in range(n):
    if a[i] == k:
        print("POSSIBLE")
        exit()
    f = fractions.gcd(f,a[i])
    
if k % f != 0:
    print("IMPOSSIBLE")
else:
    print("POSSIBLE")
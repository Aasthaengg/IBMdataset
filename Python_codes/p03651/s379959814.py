n,k = map(int,input().split())
a = list(map(int,input().split()))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if n == 1:
    gcd1 = a[0]
else:
    gcd1 = gcd(a[0], a[1])

    for i in range(2,n):
        gcd1 = gcd(gcd1,a[i])

if k > max(a):
    print('IMPOSSIBLE')
else:
    if k % gcd1 == 0:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')

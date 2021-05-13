

def gcd_core(a, b):
    if b == 0:
        return a
    else:
        return gcd_core(b, a % b)


def gcd(arr):
    g = gcd_core(arr[0], arr[1])
    for i in range(2, len(arr)):
        g = gcd_core(g, arr[i])
    return g




n,k = map(int,input().split())

if k==1:
    print(0)
else:
    print(n-k)








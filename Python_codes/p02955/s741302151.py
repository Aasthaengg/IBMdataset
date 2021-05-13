import math

def facts(n):
    sqrt_n = int(math.sqrt(n))
    fs = []
    fs_rev = []
    
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            fs.append(i)
            if n != i ** 2:
                fs_rev.append(n // i)
    
    fs.reverse()
    return fs_rev + fs

n, k = map(int, input().split())
ll = list(map(int, input().split()))
s = sum(ll)
fs = facts(s)

for f in fs:
    ll_f = list(map(lambda x: x % f, ll))
    ll_f.sort(reverse = True)
    ignore = sum(ll_f) // f
    keep = sum(ll_f[ignore:])

    if keep <= k:
        print(f)
        break
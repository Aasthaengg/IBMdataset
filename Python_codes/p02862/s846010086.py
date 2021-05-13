import sys

X, Y = map(int, input().split())
mod = int(1e9) + 7
N = 10**6
g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]


# 組み合わせ(1e9+7で割る場合)
def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod


for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

if (X + Y) % 3 != 0:
    print(0)
    sys.exit()

n = (-X + 2*Y) // 3
m = (2 * X - Y) // 3
if n < 0 or m < 0:
    print(0)
    sys.exit()

print(cmb(n+m, n, mod))

def popcount(x):
    return bin(x).count("1")

N, X = open(0).read().split()
N = int(N)
XS = list(X)
X = int(X, 2)

p = popcount(X)
xi = X % (p + 1)
if p == 1:
    xd = 0
else:
    xd = X % (p - 1)

for i in range(N):
    if XS[i] == "1":
        if p == 1:
            print(0)
            continue
        else:
            k = pow(2, N - 1 - i, p - 1)
            x = (xd - k) % (p - 1)
    else:
        k = pow(2, N - 1 - i, p + 1)
        x = (xi + k) % (p + 1)
    ans = 1
    while x != 0:
        x %= popcount(x)
        ans += 1
    print(ans)

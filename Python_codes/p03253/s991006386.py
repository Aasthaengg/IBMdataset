import math
import time

TEST = True
TEST = False


MOD = 10**9+7
n, m = map(int, input().split())
#start = time.time()

fac = [1, 1]
finv = [1, 1]
inv = [0, 1]

for i in range(2, 150000):
    fac.append(fac[i-1] * i % MOD)
    inv.append((MOD-inv[MOD%i]*(MOD//i)) % MOD)
    finv.append(finv[i-1]*inv[i]%MOD)


def binom(n, k):
    ans = (fac[n] * finv[n-k]) % MOD
    return (ans * finv[k]) % MOD


ans = 1
y = m
x = 1
while y > 1:
    if x*x > y:
        ans = (ans*binom(n,1)) % MOD
        break
    x += 1
    exp = 0
    while y % x == 0:
        y /= x
        exp += 1
    ans = (ans*binom(exp+n-1, exp)) % MOD
    if TEST:
        print("x = " + str(x) + ", ans = " + str(ans) )

print(ans)

#runTime = time.time() - start
#print("My answer is  " + str(ans))
#print("The running time is " + str(runTime) + " sec")
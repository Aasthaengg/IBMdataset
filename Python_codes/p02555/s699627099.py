import math

def comb(n, r, mod):
    return math.factorial(n + r - 1)//(math.factorial(n - 1)*math.factorial(r))%mod

s = int(input())
mod = 10**9 + 7
ans = 1

if s < 3:
    ans = 0

for i in range(2, 700): #分割数, 1の時は1通りなので除外
    if s < 3*i:
        break
    r = s - i*3
    ans = (ans + comb(i, r, mod))%mod

print(ans)

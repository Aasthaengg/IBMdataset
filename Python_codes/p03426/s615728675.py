import math
import fractions

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

def ValueToBits(x,digit):
    res = [0 for i in range(digit)]
    now = x
    for i in range(digit):
        res[i]=now%2
        now = now >> 1
    return res

def BitsToValue(arr):
    n = len(arr)
    ans = 0
    for i in range(n):
        ans+= arr[i] * 2**i
    return ans

def ValueToArray10(x, digit):
    ans = [0 for i in range(digit)]
    now = x
    for i in range(digit):
        ans[digit-i-1] = now%10
        now = now //10
    return ans
'''
def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = 2
N = 10 ** 6 + 2
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

'''

#a = list(map(int, input().split()))



h,w,d = list(map(int, input().split()))

info = []
for i in range(h):
    info.append(list(map(int, input().split())))
    
n = int(input())
qs = []
for i in range(n):
    qs.append(list(map(int, input().split())))
    
place = [[-1,-1] for i in range(h*w+1)]

for i in range(h):
    for j in range(w):
        place[info[i][j]] = [i,j]

lines = [[0] for i in range(d)]

for i in range(d):
    now = i
    dist = 0
    for j in range((h*w-i)//d):
        now += d
        p1 = place[now]
        p2 = place[now-d]
        dist += abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
        lines[i].append(dist)

for i in range(n):
    k = qs[i][0]%d
    ll = qs[i][0]//d
    rr = qs[i][1]//d
    print(lines[k][rr]-lines[k][ll])













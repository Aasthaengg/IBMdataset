N = int(input())
AB = [list(map(int,input().split())) for _ in range (N)]
MOD = 10**9+7

from collections import defaultdict
from math import gcd
def cmp(x,y):
    g = gcd(abs(x),abs(y))
    if x*y<0:
        return (-abs(x)//g, abs(y)//g)
    else:
        return (abs(x)//g, abs(y)//g)
def rev(x):
    # x = (a,b)
    # ret = (-b,a)
    a = x[0]
    b = x[1]
    if a<0:
        return (abs(b), abs(a))
    else:
        return (-abs(b), abs(a))

dnums = defaultdict(int)
dnums2 = defaultdict(int)
num_zero = 0
num_az = 0
num_bz = 0
keys = set()
for a,b in AB:
    if a!=0 and b!=0:
        k1 = cmp(a,b)
        dnums[k1] += 1
        keys.add(k1)
    elif a==0 and b==0:
        num_zero += 1
    elif a == 0 and b!=0:
        num_az += 1
    elif a != 0 and b==0:
        num_bz += 1

mydict = dict()
for key in list(keys):
    mydict[key] = False

ans = 1
for key in list(keys):
    if mydict[key]:
        continue
    rkey = rev(key)
    if rkey in keys:
        mydict[rev(key)] = True
        mydict[key] = True

    ans *= pow(2, dnums[key], MOD) + pow(2, dnums[rkey], MOD) - 1
    ans %= MOD

ans *= pow(2, num_az, MOD) + pow(2, num_bz, MOD) - 1
ans += num_zero
ans += MOD - 1
print(ans%MOD)


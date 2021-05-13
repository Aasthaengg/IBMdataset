import math
import fractions
import sys
input = sys.stdin.readline

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

def ZipArray(a):
    aa = [[a[i],i]for i in range(n)]

    aa.sort(key = lambda x : x[0])
    for i in range(n):
        aa[i][0]=i+1
    aa.sort(key = lambda x : x[1])
    b=[aa[i][0] for i in range(len(a))]
    return b

def ValueToArray10(x, digit):
    ans = [0 for i in range(digit)]
    now = x
    for i in range(digit):
        ans[digit-i-1] = now%10
        now = now //10
    return ans

def Zeros(a,b):
    if(b<=-1):
        return [0 for i in range(a)]
    else:
        return [[0 for i in range(b)] for i in range(a)]

class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
            
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

#################################################
#################################################
#################################################
#################################################


h,w,n = list(map(int, input().split()))
painted = []
for i in range(n):
    t = list(map(int, input().split()))
    for j in range(3):
        for k in range(3):
            painted.append([t[0]-2+j, t[1]-2+k])
    
painted.sort(key = lambda x : x[1])
painted.sort(key = lambda x : x[0])

p2 = []

for i in painted:
    if(i[0]>=1 and i[0]<h-1 and i[1]>=1 and i[1]<w-1):
        p2.append(i)

#print(p2)
ans = [0 for i in range(10)]
chain=0
if(len(p2)>0):
    before = p2[0]
    chain = 1
for ii in range(len(p2)-1):
    i = ii+1
    if(p2[i][0] == before[0] and p2[i][1] == before[1]):
        chain += 1
    else:
        ans[chain]+=1
        chain=1
        before[0],before[1] = p2[i]
if(len(p2)>0): ans[chain]+=1

ans[0] = (h-2)*(w-2) - sum(ans[1:])
for i in ans:
    print(i)





































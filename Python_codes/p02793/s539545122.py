import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
mod = 10**9+7
num = tuple(num)

from collections import Counter
def factorization(a):
        yy, j = [], 2
        y = yy.append
        while(a > 1):
            for i in range(j, int(a**0.5)+1):
                if a % i == 0:
                    y(i)
                    a, j = a//i, i
                    break
            else:
                y(a)
                break
        return Counter(yy)
      
def primeFactor(N):
    i, n, ret, d, sq = 2, N, {}, 2, 99
    while i <= sq:
        k = 0
        while n % i == 0: n, k, ret[i] = n//i, k+1, k+1
        if k > 0 or i == 97: sq = int(n**(1/2)+0.5)
        if i < 4: i = i * 2 - 1
        else: i, d = i+d, d^6
    if n > 1: ret[n] = 1
    return ret
  
lcd = dict()
for i in num:
  j = primeFactor(i)
  for x,y in j.items():
    if not x in lcd.keys():
      lcd[x] = y
    else:
      lcd[x] = max(lcd[x],y)

lc = 1
for i,j in lcd.items():
  lc *= pow(i,j,mod)
  
ans =0
for i in range(n):
  ans += lc*pow(num[i], mod-2, mod)
  ans %= mod
print(ans)
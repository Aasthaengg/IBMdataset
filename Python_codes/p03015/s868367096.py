import sys
input = sys.stdin.readline
L = list(map(int, list(input())[: -1]))
L.reverse()
mod = 10 ** 9 + 7
res = 1
for i in range(len(L)):
  if L[i]: res = (2 * res + pow(3, i, mod)) % mod
print(res)
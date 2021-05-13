n, k = map(int, input().split())

from math import factorial
def div(v, c):
  return factorial(v)//(factorial(max(0, v-c))*factorial(c))

for i in range(1, k+1):
  print(int(div(n-k+1, i)*div(k-1, i-1))%(10**9+7))
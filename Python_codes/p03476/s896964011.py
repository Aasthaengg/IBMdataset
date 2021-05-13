import sys
input = sys.stdin.readline

n = 10 ** 5
memo = [1] * (n+1)

for i in range(2, n):
  for j in range(2, n):
    if i * j > n:
      break
    memo[i*j] = 0
memo2 = memo[:]
memo2[1] = 0
for x in range(n+1):
  if x % 2 == 0 or memo[(x+1) // 2] == 0:
    memo2[x] = 0
  
c = [0]

for x in memo2[1:]:
  c.append(c[-1]+x)

q = int(input())
for i in range(q):
  l, r = map(int, input().split())
  print(c[r] - c[l-1])


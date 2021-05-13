import sys
input = sys.stdin.buffer.readline

def divisors(n) -> list:
  res = []
  for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
      res.append(i)
      if i != n // i:
        res.append(n // i)
  res = sorted(res)[::-1]
  return res

N, K = map(int, input().split())
A = list(map(int, input().split()))

div = divisors(sum(A))

for d in div:
  arr = []
  for a in A:
    if a % d != 0:
      arr.append(d - a % d)
    else:
      arr.append(0)
  arr = sorted(arr)[::-1]
  tmp = sum(arr[sum(arr) // d:])
  if tmp <= K:
    print(d)
    exit()
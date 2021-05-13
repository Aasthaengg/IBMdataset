import sys

def input():
  return sys.stdin.readline()[:-1]

def make_divisors(n):
  divisors = []
  for i in range(1, int(n**0.5)+1):
    if n % i == 0:
      divisors.append(i)
      if i != n // i:
        divisors.append(n//i)
  divisors.sort(reverse=True)
  return divisors

N,K = map(int, input().split())
A = list(map(int, input().split()))

sumA = sum(A)
kouho = make_divisors(sumA)

for i in kouho:
  if sumA%i != 0:
    continue
  r = [0]*N
  for j in range(N):
    r[j] = A[j]%i
  sumr = sum(r)
  if sumr%i != 0:
    continue
  r.sort(reverse=True)
  num = 0
  for k in range(sumr//i):
    num += i-r[k]
  if num <= K:
    print(i)
    exit()
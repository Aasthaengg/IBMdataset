def factorize(N):
  fCount = []
  d = 2
  while d*d <= N:
    if N % d == 0:
      cnt = 0
      while N % d == 0:
        N //= d;
        cnt += 1
      fCount.append(cnt)
    d += 1

  if N > 1: ## N is prime
    fCount.append(1)
    N = 1

  return fCount
## ----------------------
N = int(input())
arr = factorize(N)
arr.sort()  ## 2 2 3 3 3 4

def triangle(k):
  return k * (k+1)//2

smallerTriangle = [0]*45 # 2**45 > 10**12
for i in range(45):
  for j in range(1, 10000):
    if triangle(j) > i:
      smallerTriangle[i] = j-1
      break

ans = 0
for expo in arr:
  ans += smallerTriangle[expo]
print(ans)

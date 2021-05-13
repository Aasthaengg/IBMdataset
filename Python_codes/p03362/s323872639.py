n = int(input())
nmax = 55556

prime = [True]*nmax
prime[0] = prime[1] = False
for i in range(2, int(nmax**0.5)+1):
  if not prime[i]: continue
  for j in range(2*i, nmax, i):
    prime[j] = False

arr = []
for i in range(2, nmax):
  if not prime[i]: continue
  if i%10 == 3:
    arr.append(i)
    if len(arr) == n: break

print(*arr, sep=' ')
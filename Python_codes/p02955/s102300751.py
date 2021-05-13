N, K = map(int, input().split())
A = list(map(int, input().split()))

sumA = sum(A)

def make_divisors(n):
  divisors = []
  for i in range(1, int(n**0.5)+1):
    if n % i == 0:
      divisors.append(i)
      if i != n // i:
        divisors.append(n//i)
  divisors.sort()
  divisors = divisors[::-1]
  return divisors

div = make_divisors(sumA)
#print(div)

for d in div:
  tmp = []
  for a in A:
    tmp.append(a % d)
  tmp.sort()
  tmp = tmp[::-1]
  sum_tmp = sum(tmp)
  
  if sum(tmp[sum_tmp // d:]) <= K:
    print(d)
    exit()
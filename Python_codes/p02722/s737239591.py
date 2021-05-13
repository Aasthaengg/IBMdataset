n = int(input())
if n == 2:
  print(1)
  quit()
elif n == 3:
  print(2)
  quit()
def factorization(n):
  arr = []
  temp = n
  for i in range(2, int(-(-n**0.5//1))+1):
    if temp%i==0:
      cnt=0
      while temp%i==0:
        cnt+=1
        temp //= i
      arr.append([i, cnt])
  if temp!=1:
    arr.append([temp, 1])
  if arr==[]:
    arr.append([n, 1])
  return arr
ans = 1
for l in factorization(n-1):
  ans *= (l[1]+1)
def make_divisors(n):
  divisors = []
  for i in range(1, int(n**0.5)+1):
    if n % i == 0:
      divisors.append(i)
      if i != n // i:
        divisors.append(n//i)
  return divisors
lst = make_divisors(n)

for i in lst:
  if i == 1 or i == n:
    continue
  m = n
  while m % i == 0:
    m = m // i
  if m % i == 1:
    ans += 1
  
print(ans)
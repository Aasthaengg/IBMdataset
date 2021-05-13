def divisor(n):
  cd = []
  i = 1
  while i*i <= n:
    if n%i==0:
      if i*(i-1)>N:
        cd.append(i-1)
      if i != n//i and (n//i)*(n//i-1)>N:
        cd.append(n//i-1)
    i += 1
  return cd

N = int(input())
print(sum(divisor(N)))
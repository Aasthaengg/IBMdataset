N=int(input())
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors
A=make_divisors(N)
ret=0
for k in A:
  m=N//k-1
  if m>k:
    ret+=m
  else:
    break
print(ret)
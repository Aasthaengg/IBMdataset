nn = int(input())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

ans = len(make_divisors(nn-1)) - 1
lis = make_divisors(nn)
del lis[0]

for i in lis:
  t = nn
  while t%i==0 and t != 0:
    t = t//i
  if t%i == 1:
    ans += 1

print(ans)
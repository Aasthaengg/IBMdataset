def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

n, m = map(int, input().split(" "))
max = 1
#print(make_divisors(m))
for i in make_divisors(m):
  if i > m/n:
    break
  else:
    max = i
print(max)
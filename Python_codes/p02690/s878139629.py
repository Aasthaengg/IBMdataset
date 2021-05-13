x = int(input())

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

p = make_divisors(x)

for i in p:
  for b in range(-1000,1000):
    if (b+i)**5 - b**5 == x:
      print(b+i,b)
      exit()
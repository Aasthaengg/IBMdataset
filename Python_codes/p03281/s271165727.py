n = int(input())
a = 0
for j in range(n):
  j += 1
  if j % 2 != 0:
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= j:
      if j % i == 0:
        lower_divisors.append(i)
        if i != j // i:
          upper_divisors.append(j//i)
      i += 1
    if len(lower_divisors + upper_divisors[::-1]) == 8:
      a += 1
    lower_divisors.clear
    upper_divisors.clear
print(a)
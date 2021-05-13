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
n = int(input())
divs = make_divisors(n)

def judge(d):
  if n // (d-1) == n % (d-1):
    return True
  else:
    return False

ans = 0
for d in divs:
  if d > 1 and judge(d):
    ans += d-1
print(ans)


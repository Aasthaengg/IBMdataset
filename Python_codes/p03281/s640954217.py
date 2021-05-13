def mkdiv(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
ans=0
n=int(input())

for i in range(n+1):
  if len(mkdiv(i))==8 and i%2:
    ans+=1
print(ans)
def a(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
N=int(input())
L=a(N)
#N=r(m+1)
ans=0
for i in L:
  if (N//i)-1>i:
    ans+=(N//i)-1
print(ans)
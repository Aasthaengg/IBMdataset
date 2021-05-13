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
  
n=int(input())

a=make_divisors(n)

b=len(a)

if b%2==0:
  c=int(b/2)-1
  x=a[c]
  y=a[c+1]
  print(x+y-2)
  
else:
  c=int((b+1)/2)-1
  x=a[c]
  print(x+x-2)
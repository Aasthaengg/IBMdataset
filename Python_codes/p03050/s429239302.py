n=int(input())
ans=0
#約分
def make_divisors(n):  
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    # divisors.sort()
    return divisors
l=make_divisors(n)
for li in l:
  m=(n-li)//li
  if li <= m-1:
    ans+=m
print(ans)
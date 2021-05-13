# nをmで割った商および余りをdとする
# n=m*d+d
# n=(m+1)*d
# d<m
# 上記を満たす1以上のm

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    return divisors

n=int(input())
ans=0
candi=make_divisors(n)
for d in candi:
  m=n//d-1
  if d<m and 0<m:
    ans+=m
print(ans)
n=int(input())
a=list(map(int,input().split()))

a=sorted(a)

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
  
c=make_divisors(a[0])


d=sorted(c)
f=[]
for y in range(len(d)):
  e=d[y]
  ch=0
  for x in range(1,n):
    if not a[x]%e==0:
      continue
    ch+=1
  if ch==n-1:
    f.append(e)
    
print(max(f))
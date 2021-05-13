def gcd(a,b):
  while a>0 and b>0:
    if a>b:a%=b
    else: b%=a
  return max(a,b)

a,b =(int(i) for i in input().split())
print((a*b)//gcd(a,b))
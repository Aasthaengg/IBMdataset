a,b,k=map(int,raw_input().split(' '))
for i in range(k):
  a &= 0x7ffffffe
  b += a/2
  a /= 2
  b,a=a,b
if k%2:
  b,a=a,b
print a,b

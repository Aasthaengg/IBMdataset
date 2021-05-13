N=int(input())
a=2
b=1
for x in range(N-1):
  c=b
  b=a+b
  a=c
print(b)
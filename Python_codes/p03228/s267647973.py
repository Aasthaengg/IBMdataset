a,b,k=map(int, input().split())
while True:
  if k< 1:
    break
  if a %2==1:
    a=a-1
  c = a // 2
  a = c
  b = b + c
  k=k-1
  if k<1:
    break
  if b %2==1:
    b=b-1
  b = b//2
  a = a + b
  k=k-1
  #print(a,b,k)
print(a, b)
x=int(input())
def f(n):
  a=100
  for i in range(0,n):
    a+=a//100
  return(a)

for i in range(10**18):
  if f(i)>=x:
    print(i)
    break
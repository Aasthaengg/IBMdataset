n=int(input())
x=1
for i in range(1,n+1):
  x*=i
  if x>1000000007:
    x%=1000000007
print(x)
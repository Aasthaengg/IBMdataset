a,b=map(int,input().split())
d=len(str(b))
A=a*10**d+b
for i in range(1,350):
  if i**2==A:
    print('Yes')
    exit()
print('No')
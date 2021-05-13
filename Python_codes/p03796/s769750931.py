c=int(input())
p=1
m=10**9+7
for i in range(2,c+1):
  p=(p*i)%m
print(p)
a,b,k=map(int,input().split())
for i in range(k):
  if i % 2 == 0 and a % 2 ==1:
    a=(a-1)//2
    b+=a
  elif i % 2 ==0 and a%2==0:
    a=a//2
    b+=a
  elif i%2==1 and b%2==1:
    b=(b-1)//2
    a+=b
  else:
    b=b//2
    a+=b
print(a,b)
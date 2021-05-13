n=int(input())
c=0
m=n/2
while m>=5:
  m/=5
  c+=1
sm=0
for i in range(c):
  sm+=(n//2)//(5**(i+1))
print(sm if n%2==0 else 0)
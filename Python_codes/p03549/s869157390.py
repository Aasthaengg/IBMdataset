N, M=map(int, input().split())
r=(N-M)*100+M*1900
p=1/2**M
q=1-p
ans=0
for i in range(1,10000):
  ans+=(r*i)*p*q**(i-1)
if ans-int(ans)>0.5:
  print(int(ans)+1)
else:
  print(int(ans))
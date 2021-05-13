N=int(input())
ans=0
for i in range(3):
  n=N%10
  N=N//10
  ans+=10**i*((n+8)%16)
print(ans)
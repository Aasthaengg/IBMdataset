N,M = map(int,input().split())
D = sorted([list(map(int,input().split())) for n in range(N)])
ans = 0
num = 0

for a,b in D:
  num+=b
  ans+=a*b
  if M<=num:
    ans-=a*(num-M)
    break

print(ans)
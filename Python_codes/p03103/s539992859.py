N, M=map(int, input().split())
info=[]
for _ in range(N):
  a, b=map(int, input().split())
  info.append([a,b])

info.sort(key=lambda x:x[0])
ans=0
for a, b in info:
  if M>=b:
    ans+=a*b
    M-=b
  elif M<b and M>0:
    ans+=a*M
    break
  else:
    break
print(ans)
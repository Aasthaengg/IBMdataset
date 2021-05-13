N,M=map(int, input().split())
A=[list(map(int, input().split())) for i in range(N)]
B=[]
for x,y,z in A:
  a=x+y+z
  b=x+y-z
  c=x-y+z
  d=x-y-z
  e=-x+y+z
  f=-x+y-z
  g=-x-y+z
  h=-x-y-z
  B.append([a,b,c,d,e,f,g,h])
ans=0
for i in range(8):
  D=sorted(B,reverse=True,key=lambda x:x[i])
  d=0
  for j in range(M):
    d+=D[j][i]
  ans=max(ans,d)
print(ans)
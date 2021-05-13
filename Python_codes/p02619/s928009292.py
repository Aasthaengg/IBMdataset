D=int(input())
c=list(map(int,input().split()))
s=[]
for _ in range(D):
  s.append(list(map(int,input().split())))
t=[]
for _ in range(D):
  t.append(int(input()))
g=0
for d in range(D):
  a=s[d][t[d]-1]
  b=0
  for i in range(26):
    for j in range(d+1,0,-1):
      if t[j-1]==i+1:
        b+=c[i]*(d+1-j)
        break
    else:
      b+=c[i]*(d+1)
  g+=a-b
  print(g)
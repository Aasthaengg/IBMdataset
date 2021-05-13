n=int(input())
F=[]
for i in range(n):
  F.append(list(map(int,input().split())))
P=[]
for i in range(n):
  P.append(list(map(int,input().split())))
maxp=-10**11
for i in range(1,2**10):
  prof=0
  s='{0:b}'.format(i)
  S=[]
  for i in range(len(s)):
    S.append(s[i])
  S.reverse()
  for i in range(10-len(s)):
    S.append('0')
  S.reverse()
  for j in range(n):
    count=0
    for k in range(10):
      count+=int(S[k])*F[j][k]
    prof+=P[j][count]
  maxp=max(maxp,prof)
print(maxp)

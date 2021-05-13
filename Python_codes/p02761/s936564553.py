p = 0
t = 0
N,M = map(int, input().split())
s = []
c = []
for i in range(M):
  s.append(0)
  c.append(0)
for i in range(M):
  s[i], c[i]=map(int, input().split())
number=[1]
for k in range(N-1):
  number.append(10)
for i in range(M):
  for j in range(M):
    if (s[i]==s[j]) and (c[i]!=c[j]):
      p = 1
for i in range(M):
  number[s[i]-1]=c[i]
number = [0 if z==10 else z for z in number]
h = 0
k = 0
while h<=M-1 and k==0:
  k=1
  if c[h]==0:
    k = 0
  h+=1
if N==1 and h==M and k!=1:
  p = 2
if number[0]==0 and N!=1 and p!=2:
  p=1
if p==0:
  for i in range(N):
    print(number[i], end="")
if p==1:
  print(-1)
if p==2:
  print(0)
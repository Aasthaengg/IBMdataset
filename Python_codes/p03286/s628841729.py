N=int(input())
if N==0:
  print(0)
  exit()
X=1
P=''
for i in range(32):
  if N&X:
    if i&1:
      N+=X
    else:
      N-=X
    P+='1'
  else:
    P+='0'
  X<<=1
while P[-1]=='0':
  P=P[:-1]
print(P[::-1])
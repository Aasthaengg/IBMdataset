n=int(input())
a=list(map(int,input().split()))
q=int(input())
m=list(map(int,input().split()))
b=[0]*2**n
for i in range(2**n):
  tr=bin(i)[2:].zfill(n)
  cnt=0
  for j in range(n):
    if tr[j]=='1':
      cnt+=a[j]
  b[i]=cnt
for i in m:
  if i in b:
      print('yes')
  else:
      print('no')

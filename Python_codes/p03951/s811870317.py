n=int(input())
s=input()
t=input()
actualfail=0
for i in range(n):
  fail=0
  for j in range(n-i):
    if s[i+j]!=t[j]:
      fail=1
      break
  if fail==0:
    actualfail=1
    break
if actualfail==1:
  print(n+i)
else:
  print(2*n)
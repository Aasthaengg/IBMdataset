import sys
s=input()
k=int(input())
if k<=100:
  if s[:k]=='1'*k:
    print(1)
    sys.exit()
for i in s:
  if i!='1':
    print(i)
    break
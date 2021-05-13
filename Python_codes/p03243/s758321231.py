import sys
n=input()
n=list(n)

if n[0]>n[1]:
  print(n[0]*3)
  sys.exit()

if n[0]<n[1]:
  print(str((int(n[0])+1))*3)
  sys.exit()
  
if n[0]==n[1]>=n[2]:
  print(n[0]*3)
  sys.exit()

if n[0]==n[1]<n[2]:
  print(str((int(n[0])+1))*3)
  sys.exit()

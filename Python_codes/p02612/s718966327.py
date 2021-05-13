N=int(input())
if N%1000!=0:
  S=N%1000
else:
  S=1000

print(1000-S)

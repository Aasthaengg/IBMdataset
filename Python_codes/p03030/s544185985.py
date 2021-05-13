n=int(input())
R=[]
for i in range(n):
  s,p=input().split()
  R.append([s,100-int(p),i+1])
R.sort()
for r in R:
  print(r[2])
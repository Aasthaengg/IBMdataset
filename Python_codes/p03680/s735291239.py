n=int(input())
a=[int(input())-1 for _ in range(n)]
i=0
ct=0
while i!=1:
  if a[i]==-1:
    print("-1")
    break
  k=i
  i=a[i]
  a[k]=-1
  ct+=1
else:
  print(ct)
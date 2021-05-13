N=input()
N=int(N)
ls=[int(s) for s in input().split()]
count=0
for i in range(N):
  if ls[i]==i+1:
    count=count+1
if count>=N-2:    
  print("YES")
else:
  print("NO")
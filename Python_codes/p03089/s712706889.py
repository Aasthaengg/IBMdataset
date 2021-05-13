n=int(input())
b=[int(_) for _ in input().split()]

ans=[]
for i in range(n):
  for j in range(n-i-1,-1,-1):
    if b[j]==j+1:
      b.pop(j)
      ans.append(j)
      break
  else:
      print(-1)
      exit()
      
for i in reversed(ans):
  print(i+1)
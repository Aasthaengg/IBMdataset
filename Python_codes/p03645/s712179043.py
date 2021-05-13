n,m=map(int,input().split())
ans = set()
for i in range(m):
  a,b=map(int,input().split())
  if a == 1:
    if b in ans:
      print("POSSIBLE")
      break
    else:
      ans.add(b)
  if b == n:
    if a in ans:
      print("POSSIBLE")
      break
    else:
      ans.add(a)
else:
  print("IMPOSSIBLE")
a,b = map(int,input().split())


ans = (a+b)/2

if ans.is_integer() == True:
  print(int(ans))
else:
  print("IMPOSSIBLE")
A,B,X=map(int,input().split())
if A>X:
  print("NO")
elif A==X:
  print("YES")
elif (X-A)<=B:
  print("YES")
else:
  print("NO")
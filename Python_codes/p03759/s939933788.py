def is_beautiful(a,b,c):
  return b-a==c-b

a,b,c=map(int,input().split())
if is_beautiful(a,b,c):
  print("YES")
else:
  print("NO")
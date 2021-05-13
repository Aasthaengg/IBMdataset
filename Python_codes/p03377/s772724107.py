a,b,c = map(int, input().split())
if a > c:
  print("NO")
elif c-a <= b:
  print("YES")
else:
  print("NO")
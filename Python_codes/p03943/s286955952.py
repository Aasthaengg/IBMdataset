a,b,c = map(int,input().split())
ans = 0
if a+b == c:
  ans += 1
elif a+c == b:
  ans += 1
elif b+c == a:
  ans += 1
if ans >0:
  print("Yes")
else:
  print("No")

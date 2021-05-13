a,b,c = map(int,input().split())
ans = 0

if a == b and a == c and a%2 == 0:
  print("-1")
elif a == b and a == c and a%2 == 0:
  print(0)
else:
  while a%2 == 0 and b%2 == 0 and c%2 == 0:
    ans += 1
    aa = b/2 + c/2
    bb = a/2 + c/2
    cc = a/2 + b/2
    a = aa
    b = bb
    c = cc
  print(ans)
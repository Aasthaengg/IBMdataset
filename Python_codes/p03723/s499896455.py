a,b,c = map(int,input().split())
ans = 0
if a%2 == 1 or b%2 == 1 or c%2 == 1:
  ans = 0
elif a == b and b == c:
  ans = -1
else:
  while a%2 != 1 and b%2 != 1 and c%2 != 1:
    aa = b/2 + c/2
    bb = c/2 + a/2
    cc = a/2 + b/2
    a = int(aa)
    b = int(bb)
    c = int(cc)
    ans += 1
print(ans)  
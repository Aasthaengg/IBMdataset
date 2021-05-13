a,b,c = map(int,input().split())
ans = 0
if a>=c:
  ans += c+b
else:
  ans += a
  if b>=(c-a):
    ans += b+c-a
  else:
    ans += 2*b+1
print(ans)
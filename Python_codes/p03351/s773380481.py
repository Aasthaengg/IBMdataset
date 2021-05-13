a,b,c,d =map(int, input().split())
ans="No"
if abs(a-c)<=d:
  ans ="Yes"
if a<=b<=c or c<=b<=a:
  if abs(a-b)<=d and abs(c-b)<=d:
    ans="Yes"
print(ans)

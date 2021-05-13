n = str(input())
dix = {'1':'9','9':'1'}
ans = ""
for x in n:
  if x=='1' or x=='9':
    ans += dix[x]
  else:
    ans += x
print(ans)

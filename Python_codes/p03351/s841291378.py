a,b,c,d = map(int,input().split())
ans = 'No'
if max(a,c)-min(a,c)<=d:
  ans = 'Yes'
if max(a,b)-min(a,b)<=d and max(b,c)-min(b,c)<=d:
  ans = 'Yes'
print(ans)
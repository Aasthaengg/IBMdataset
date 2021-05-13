x,y = map(int,input().split())
ans = 'No'
for i in range(x+1):
  tu = i
  cr = x - i
  ch = tu*4 + cr*2
  if ch == y:
    ans = 'Yes'
    break
print(ans)
h,w,a,b = map(int,input().split())
ans = [''] * h
for i in range(h):
  if i < b :
    ans[i] = '0'*a + '1'*(w-a)
  else:
    ans[i] = '1'*a + '0'*(w-a)
for s in ans:
  print(s)

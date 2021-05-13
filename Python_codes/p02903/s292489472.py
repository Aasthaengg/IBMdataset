h,w,a,b=map(int,input().split())
ans = [""] * h
for i in range(h):
  s = ""
  if i < b:
    s = "0" * a + "1" * (w - a)
  else:
    s = "1" * a + "0" * (w - a)
  ans[i] = s

print('\n'.join(ans))
      

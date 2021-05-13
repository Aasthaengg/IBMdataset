h,w,a,b = map(int,input().split())
ans = []

for i in range(h):
  if i+1 <= b:
    s = "0"*a + "1"*(w-a)
  else:
    s = "1"*a + "0"*(w-a)
    
  ans.append(s)
  
for i in range(h):
  print(ans[i])
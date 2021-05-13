w,h,n =map(int,input().split())
s =[list(map(int,input().split())) for _ in range(n)]
x =0;y =0;
for i in range(n):
  if s[i][2] ==1:
    if x < s[i][0]: x = s[i][0] 
  elif s[i][2] ==2:
    if w > s[i][0]: w = s[i][0]
  elif s[i][2] ==3:
    if y < s[i][1]: y = s[i][1]
  else:
    if h > s[i][1]: h = s[i][1]
print((w-x)*(h-y) if (w-x)>0 and (h-y)>0 else 0) 
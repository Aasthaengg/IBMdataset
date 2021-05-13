W,a,b=map(int,input().split())
thre =0 
res =0
if a<=b:
  thre = a+W
  if thre >= b:
    res = 0
  else:
    res = b-thre
else:
  thre=b+W
  if thre >= a:
    res = 0
  else:
    res = a-thre
print(res)
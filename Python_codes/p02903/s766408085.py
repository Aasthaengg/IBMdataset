h,w,a,b=map(int,input().split())
l=[[] for i in range(h)]
mode=True
for i in range(h):
  if i>=b:
    mode=False
  for j in range(w):
    if mode:
      if j<a:l[i].append("1")
      else:l[i].append("0")
    else:
      if j<a:l[i].append("0")
      else:l[i].append("1")
for li in l:
  print("".join(li))
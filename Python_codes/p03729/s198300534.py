a,b,c=map(str,input().split())
Flag = 1
if a[len(a)-1]!=b[0]:
  Flag =0
if b[len(b)-1]!=c[0]:
  Flag =0
if Flag == 0:
  print("NO")
else:
  print("YES")
a,b,c = map(str,input().split())

flag = False

if a[-1] == b[0]:
  if b[-1] == c[0]:
    flag = True

if flag == True:
  print("YES")
else:
  print("NO")
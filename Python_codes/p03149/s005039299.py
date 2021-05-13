n = list(input().split())
myStr = "1974"

if len(set(n))==4 and n[0] in myStr and n[1] in myStr and n[2] in myStr and n[3] in myStr:
  print("YES")
else:
  print("NO")
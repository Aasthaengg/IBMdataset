s=input()
l=list("1 9 7 4".split())
flg=True
for i in l:
  if i not in s:
    flg=False
    break

if flg:
  print("YES")
else:
  print("NO")
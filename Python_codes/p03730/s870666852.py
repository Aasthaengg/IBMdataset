a,b,c=map(int,input().split())
amari = []
flag = True
i = 0
FLAG = False
while flag:
  check = b*i+c
  if check % a ==0:
    FLAG = True
    flag = False
  else:
    if 0 == amari.count(check % a):
      amari.append(check%a)
    else:
      flag = False
  i = i + 1
if FLAG:
  print("YES")
else:
  print("NO")
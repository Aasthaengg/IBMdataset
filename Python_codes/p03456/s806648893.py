a,b = map(str,input().split())
c = int(a+b)
flag = True
for i in range(100200):
  if i**2 == c:
    print("Yes")
    flag = False
    break
if flag:
  print("No")
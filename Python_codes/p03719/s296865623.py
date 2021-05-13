A, B, C = map(int,input().split())
 
flag = False
 
if A <= C:
  if B>= C:
    flag = True

if flag == True:
  print("Yes")
else:
  print("No")
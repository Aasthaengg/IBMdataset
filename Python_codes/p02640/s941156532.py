x,y = map(int,input().split())
flag = 0
for i in range(x+1):
  if (y - 2*i)%4 == 0 and (y -  2 * i)//4 == x - i:
    flag += 1
    print("Yes")
    break
if flag == 0:
  print("No")
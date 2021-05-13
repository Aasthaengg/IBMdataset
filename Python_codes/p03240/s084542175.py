n = int(input())
x_y_h_list = []
for i in range(n):
  x_y_h_list.append(list(map(int,input().split())))
x_y_h_list.sort(key=lambda x: x[2],reverse = True)
result = []
for x in range(101):
  for y in range(101):
    H = -1
    check = True
    for x_y_h in x_y_h_list:     
      if H == -1:
        H = x_y_h[2] + abs(x_y_h[0] - x) + abs(x_y_h[1] - y)
      else:
        if x_y_h[2] != 0:
          if H != x_y_h[2] + abs(x_y_h[0] - x) + abs(x_y_h[1] - y):
            check = False
            break
        else:
          if H > abs(x_y_h[0] - x) + abs(x_y_h[1] - y):
            check = False
            break
    if check == True:
      print(x,y,H)
     
        
     
   
        

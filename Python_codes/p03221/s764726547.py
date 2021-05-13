n, m = list(map(int, input().split()))
yp = []
for i in range(m):
  y, p = list(map(int, input().split()))
  yp.append([i+1, y, p])
  
yp.sort(key=lambda x: x[2])
counter = [1]*n
for i in range(m):
  num1 = "0"*(6-len(str(yp[i][1]))) + str(yp[i][1])
  junban = str(counter[yp[i][1]-1])
  counter[yp[i][1]-1] += 1
  num2 = "0"*(6-len(junban)) + junban
  yp[i].append(num1+num2)
  
yp.sort(key=lambda x: x[0])
for i in range(m):
  print(yp[i][3])
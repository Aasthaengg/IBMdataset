i = [int(input()) for i in range(4)]

if i[0]<i[1]:
  train = i[0]
elif i[1]<=i[0]:
  train = i[1]
  
if i[2]<i[3]:
  bus= i[2]
elif i[3]<=i[2]:
  bus= i[3]

print(train+bus)
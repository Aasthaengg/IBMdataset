line = input().split()
line2 = input().split()

num = int(line[0])
lim = int(line[1])

x = 0
for i in range(num):
  if int(line2[i]) >= lim:
    x += 1
    
print(x)
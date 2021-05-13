x = int(input())

c = 100
y = 0

while c < x:
  y += 1
  c += (c // 100)
  
print(y)

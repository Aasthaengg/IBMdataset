x, y = map(int, input().split())
z = x
i = 0
while z <= y:
  z = z * 2
  i += 1
  if z > y:
    break 
print(i)
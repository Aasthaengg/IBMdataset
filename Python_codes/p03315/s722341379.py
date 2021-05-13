n = str(input())

x = 0

for i in range(4):
  if n[i] == "+":
    x = x + 1
  else:
    x = x - 1
    
print(x)


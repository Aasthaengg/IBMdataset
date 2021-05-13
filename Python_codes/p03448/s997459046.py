a = int(input())
b = int(input())
c = int(input())
x = int(input())

combination = []
for A in range(a+1):
  for B in range(b+1):
    for C in range(c+1):
      total = A*500 + B*100 + C*50
      combination.append(total)

count = combination.count(x)
print(count)
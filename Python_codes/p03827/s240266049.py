n = int(input())
a = []
b = input()
x = 0
a.append(0)
for i in range(n):
  if b[i] == "I":
    x += 1
  else:
    x -= 1
  a.append(x)
  
print(max(a))
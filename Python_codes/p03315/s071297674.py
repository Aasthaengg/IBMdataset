a = list(input())
count = 0
for i in range(4):
  if a[i] == "+":
    count += 1
  elif a[i] == "-":
    count -= 1

print(count)
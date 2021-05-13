num = int(input())
new = input()

x = 0
m = 0
for i in range(num):
  if new[i] == "D":
    x -= 1
  if new[i] == "I":
    x += 1
  if m < x:
    m = x
print(m)

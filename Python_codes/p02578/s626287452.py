a = input()
b = list(map(int,input().split()))
x = 0
y = 0
for i in b:
  if i <= x:
    y += x - i
  else:
    x = i
print(y)
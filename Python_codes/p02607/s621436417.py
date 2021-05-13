x = input()
data = list(map(int, input().split()))
t = 0
num = 0
for i in data:
  if t % 2 == 0 and i % 2 == 1:
    num += 1
  t += 1
print(num)
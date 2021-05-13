res = 0
num = int(input())
for i in range(1, num + 1):
  if len(str(i)) % 2 != 0:
    res += 1
print(res)
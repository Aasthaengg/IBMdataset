splited = input().split(" ")

k = int(splited[0])
s = int(splited[1])

result = 0
for x in range(k+1):
  for y in range(k+1):
    z = s - x - y
    if 0 <= z and z <= k:
      result = result + 1

print(result)

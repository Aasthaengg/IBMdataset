n = int(input())
result = 0

for i in range(n):
  l = input().split(' ')
  result = result + int(l[1]) - int(l[0]) + 1

print(result)
n = int(input())
x = [input().split() for i in range(n)]
count = 0
for i in x:
  if i[1] == 'BTC':
    count += float(i[0])*380000
  else:
    count += int(i[0])
print(count)
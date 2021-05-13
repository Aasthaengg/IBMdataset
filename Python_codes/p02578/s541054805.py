n = int(input())
a = list(map(int, input().split()))

result = 0
tmp = a[0]

for i in range(1, n): 
  if tmp >= a[i]: 
    result += tmp - a[i]
  else: 
    tmp = a[i]

print(result)
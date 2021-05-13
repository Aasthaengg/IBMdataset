n = int(input())
p = list(map(int, input().split()))

count = 0
for i in range(n-1):
  if int(i+1) == p[i]:
    p1 = p[i]
    p[i] = p[i+1]
    p[i+1] = p1
    count += 1
else:
  if n == p[n-1]:
    count += 1
print(count)
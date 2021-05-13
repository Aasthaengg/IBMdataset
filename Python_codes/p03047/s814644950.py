N, K = map(int, input().split())
l = []
count = 0
j = 0
for i in range(1,N+1):
  l.append(i)
while True:
  j += 1
  if j + K-2 >= len(l):
    break
  count += 1
print(count)
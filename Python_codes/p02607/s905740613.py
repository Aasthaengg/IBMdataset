N = int(input())
a = [int(i) for i in input().split(" ")]

count = 0
for i in range(0, N):
  if i % 2 == 1:
    continue
  if a[i] % 2 == 0:
    continue
  count += 1
    
print(count)
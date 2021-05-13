n = int(input())
l = list(map(int, input().split()))

count = 0
for i in range(n):
  x = l[i]
  if l[x-1]-1 == i:
    count += 1

count = count//2
print(int(count))
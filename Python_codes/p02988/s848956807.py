n = int(input())
p = list(map(int, input().split()))
count = 0
for i in range(1, n-1):
  num = [p[i-1], p[i], p[i+1]]
  if (max(num) == num[0] or max(num) == num[2]) and\
  (min(num) == num[0] or min(num) == num[2]):
    count += 1
print(count)
n = int(input())
A = list(map(int, input().split()))
A.sort()

total = 0
count = 1
for i in range(1, n):
  if 2 * (A[i - 1] + total) >= A[i]:
    count += 1
  else:
    count = 1
  total += A[i - 1]
print(count)
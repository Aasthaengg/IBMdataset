n = int(input())
A = list(map(int, input().split()))
B = [0] * n
ret = []
for i in range(n):
  j = n - i - 1
  count = A[j]
  num = j + 1
  while True:
    num += (j + 1)
    if num > n:
      break
    count += B[num - 1]
  if count % 2:
    B[j] = 1
    ret.append(j + 1)
print(len(ret))
print(*ret)
N = int(input())
numbers = [int(x) for x in input().split()]
numbers.sort()

csum = [0] * (N + 1)

for i in range(N):
  csum[i + 1] = csum[i] + numbers[i]

count = 1  # 一番大きい数は常にOK

for i in range(N - 1, -1, -1):
  if csum[i] * 2 < numbers[i]:
    break
  count += 1
  
print(count)  

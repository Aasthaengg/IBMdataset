N, M = map(int, input().split())
nums = []
for n in range(1, int(M**0.5)+1):
  if M%n == 0:
    nums.append(n)
    nums.append(M//n)
nums.sort()
answer = 1
for num in nums:
  if M//num < N:
    break
  else:
    answer = num
print(answer)
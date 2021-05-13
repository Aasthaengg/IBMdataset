N = int(input())
nums = list(map(int, input().split()))
answer = 10**8
for p in range(1, 100):
  power = 0
  for j in range(N):
    power += (p-nums[j])**2
  answer = min(answer, power)
print(answer)
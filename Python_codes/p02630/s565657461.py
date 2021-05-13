N = int(input())
nums = list(map(int, input().split()))
Q = int(input())
operations = [list(map(int, input().split())) for _ in range(Q)]

counts = [ 0 for __ in range(10**5+1)]
answer = sum(nums)

for num in nums:
  counts[num] += 1

for b, c in operations:
  answer += counts[b]*(c-b)
  print(answer)
  counts[c] += counts[b]
  counts[b] = 0


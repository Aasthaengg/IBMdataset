N = int(input())
nums = list(map(int, input().split()))
counts = [0 for _ in range(N+1)]
for num in nums:
  counts[num] += 1
combination = 0
for count in counts:
  if count >= 2:
    combination += (count*(count-1))//2
for num in nums:
  print(combination-counts[num]+1)

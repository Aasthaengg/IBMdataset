expected = {}

n, k = [int(i) for i in input().split(" ")]
p = [int(i) for i in input().split(" ")]

max_sum = 0
for i in range(k):
  max_sum += p[i]
  
last_sum = max_sum
max_init_index = 0

for i in range(1, n - k + 1):
  current_sum = last_sum - p[i - 1] + p[i + k - 1]
  if max_sum < current_sum:
    max_sum = current_sum
    max_init_index = i
  last_sum = current_sum

for i in range(1, 1001):
  expected[i] = 1 + (i - 1)/2

ans = 0
for i in range(max_init_index, max_init_index + k):
  ans += expected[p[i]]

print(ans)
  


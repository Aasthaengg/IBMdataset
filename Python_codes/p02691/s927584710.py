import bisect
N = int(input())
A = [0] + [int(i) for i in input().split()]

sum_list = [i + A[i] for i in range(1, N+1)]
sum_list.sort()

count = 0
for i in range(1, N+1):
  v = i - A[i]
  idx_right = bisect.bisect_right(sum_list, v)
  idx_left = bisect.bisect_left(sum_list, v)
  if idx_right > 0 and sum_list[idx_right-1] == v:
    count += idx_right - idx_left
print(count)

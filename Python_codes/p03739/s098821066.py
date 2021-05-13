N = int(input())
A = list(map(int, input().split()))
B = A[:]

# evenがプラスの時
sum_even = 0
ans_even = 0

for i in range(N):
  sum_even += A[i]
  if i % 2 == 0:
    if sum_even <= 0:
      ans_even += abs(sum_even) + 1
      sum_even += abs(sum_even) + 1
  else:
    if sum_even >= 0:
      ans_even += abs(sum_even) + 1
      sum_even -= abs(sum_even) + 1

# oddがプラスの時
sum_odd = 0
ans_odd = 0
for i in range(N):
  sum_odd += A[i]
  if i % 2 == 1:
    if sum_odd <= 0:
      ans_odd += abs(sum_odd) + 1
      sum_odd += abs(sum_odd) + 1
  else:
    if sum_odd >= 0:
      ans_odd += abs(sum_odd) + 1
      sum_odd -= abs(sum_odd) + 1

answer = min(ans_even, ans_odd)
print(str(answer))

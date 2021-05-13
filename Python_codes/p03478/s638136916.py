N, A, B = list(map(int, input().split()))

r_sum = 0
for i in range(1, N+1):
  sum_digit = 0
  n_str = str(i)
  for j in range(len(n_str)):
    sum_digit += int(n_str[j])
  if A <= sum_digit and sum_digit <= B:
    r_sum += i
print(str(r_sum))
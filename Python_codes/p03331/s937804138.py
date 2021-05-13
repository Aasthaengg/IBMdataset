N = int(input())

def digit_sum(num):
  digit_sum = 0
  while(num > 0):
    digit_sum += num % 10
    num = int(num / 10)
  return digit_sum

min_num = 100000
for A in range(1, N):
  B = N - A
  digit_num = digit_sum(A)
  digit_num += digit_sum(B)
  if digit_num < min_num:
    min_num = digit_num

print(min_num)
N = int(input())
N_half = N//2

min_sum = N

for A in range(1,N_half+1):
  digit_a = 0
  digit_b = 0
  B = N-A
  while A!=0:
    num = A%10
    digit_a += num
    A = A//10
  while B!=0:
    num = B%10
    digit_b += num
    B = B//10
  digit = digit_a + digit_b
  if digit<min_sum:
    min_sum = digit

print(min_sum)
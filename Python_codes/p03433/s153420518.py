N = int(input())
A = int(input())
if N > A:
  while N > 500:
    N %= 500
print('Yes' if N <= A else ('No'))
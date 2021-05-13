N = int(input())
if N == 0:
  print(0)
  quit()

S = ''
while N != 0:
  if N % 2 == 0:
    S += '0'
    N //= -2
  else:
    S += '1'
    N -= 1
    N //= -2

print(S[::-1])
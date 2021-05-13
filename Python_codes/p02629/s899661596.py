N = int(input())
alpha = 'abcdefghijklmnopqrstuvwxyz'
ans = ''

while N > 0:
  N = N - 1
  ans = alpha[N%26] + ans
  N = N//26

print(ans)
N = int(input())

ans = ''
m = 2
i = 0

while 1:
  if N % m != 0:
    ans += '1'
    N = N - (-2)**i
  else:
    ans += '0'
  m *= 2
  i += 1
  if N == 0:
    break

print(ans[::-1])

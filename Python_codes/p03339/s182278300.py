n = int(input())
s = input()

accum_w = [0] * (n+1)  # accum_w[i] = (s[:i].count('W'))
accum_e = [0] * (n+1)  # accum_e[i] = (s[i:].count('E'))

cnt_w = 0
for i in range(n):
  if s[i] == 'W':
    cnt_w += 1
  accum_w[i+1] = cnt_w

cnt_e = 0
for j in range(n-1, -1, -1):
  if s[j] == 'E':
    cnt_e += 1
  accum_e[j] = cnt_e

# print(accum_w)
# print(accum_e)

ans = 2**64-1
for i in range(n):
  ans = min(ans, accum_w[i]+accum_e[i+1])

print(ans)

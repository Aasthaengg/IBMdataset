N, K = map(int, input().split())
A = list(map(int, input().split()))
max_length = max(max(A), K).bit_length()
A_bin = [bin(a)[2:].zfill(max_length) for a in A]
K_bin = bin(K)[2:].zfill(max_length)

count = []
for digit in range(max_length):
  count_zero = 0
  for a_bin in A_bin:
    if a_bin[digit] == '0':
      count_zero += 1
  count.append(count_zero)


half = -(-N//2)
X = ''
tight = True
for i, c in enumerate(count):
  if c < half:
    X += '0'
    if K_bin[i] == '1':
      tight = False
  else:
    if K_bin[i] == '1' or not tight:
      X += '1'
    else:
      X += '0'


X = int(X, 2)
ans = 0
for a in A:
  ans += X^a


print(ans)
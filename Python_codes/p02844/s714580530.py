N = int(input())
S = input()
R = S[::-1]

count = 0

for v in range(1000):
  V = str(v).zfill(3)
  right = -1
  left = -1
  if V[2] in R:
    r = R.index(V[2]) + 1
    right = N-r
  else:
    continue
  if V[0] in S:
    left = S.index(V[0]) + 1
  else:
    continue
  if V[1] in S[left:right]:
    count += 1

print(count)
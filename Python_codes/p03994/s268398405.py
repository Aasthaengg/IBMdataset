S = input()
K = int(input())

A = [" " for _ in range(len(S))]

zan = K
for i in range(len(S)):
  n = (ord('z') - ord(S[i]) + 1) % 26 # aに変換するのに必要な回数
  if zan >= n:
    zan -= n
    A[i] = 'a'
  else:
    A[i] = S[i]

if zan > 0:
  A[-1] = chr((ord(A[-1]) - ord('a') + zan)%26 + ord('a'))
print("".join(A))
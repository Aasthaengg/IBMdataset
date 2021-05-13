S = input()

# 後ろから削除したいので、反転して前から削除する
S = S[::-1] 
words = {'maerd', 'remaerd', 'esare', 'resare'}

while len(S) > 0:
  orig = S
  for w in words:
    if S.startswith(w):
      S = S[len(w):]
      break
  if orig == S:
    break

if len(S) == 0: print('YES')
else: print('NO')
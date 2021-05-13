S = input()
N = len(S)

cnt = 0
i = 0
j = N-1
while i < j:
  if S[i] == 'x':
    if S[j] == 'x':
      i += 1
      j -= 1
    else:
      i += 1
      cnt += 1
  else:
    if S[i] == S[j]:
      i += 1
      j -= 1
    elif S[j] == 'x':
      cnt += 1
      j -= 1
    else:
      print(-1)
      exit()
print(cnt)
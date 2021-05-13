S = input()
N = len(S)
si, ei = 0, N-1
cnt = 0
while si<ei:
  if S[si] != S[ei]:
    if S[si] == 'x':
      si += 1
      cnt+=1
    elif S[ei] == 'x':
      ei -= 1
      cnt+=1
    else:
      print(-1)
      exit()
  else:
    si += 1
    ei -= 1
print(cnt)
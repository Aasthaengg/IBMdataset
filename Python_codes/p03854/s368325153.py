S = input()[::-1]
text = ['dream','dreamer','erase','eraser']
text = [t[::-1] for t in text]

while len(S) > 0:
  for t in text:
    if S.find(t) == 0:
      S = S[len(t):]
      break
  else:
    print('NO')
    break
else:
  print('YES')
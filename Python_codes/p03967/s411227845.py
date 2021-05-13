S = input()

cnt = 0
for s in S:
  if s == 'g':
    cnt += 1

if len(S) % 2 == 1:
  print(cnt-len(S)//2-1)
else:
  print(cnt-len(S)//2)
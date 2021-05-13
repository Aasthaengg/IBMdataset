S = input()
K = int(input())
 
for i, s in enumerate(S, 1):
  if s == '1':
    if i == K:
      print(s)
      break
    else:
      continue
  else:
    print(s)
    break
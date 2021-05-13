S = input()
alphabets = [chr(x + ord('a')) for x in range(26)]
if len(S) < 26:
  n = min(set(alphabets) - set(s for s in S))
  print(S+n)
else:
  current = 'a'
  done = False
  for i in range(26):
    if S[25-i] < current:
      n = min(s for s in S[25-i+1:] if s > S[25-i])
      #sub = [s for s in S[25-i:]]
      #sub.remove(n)
      print(S[:25-i] + n )#+ ''.join(sorted(s for s in sub)))
      done = True
      break
    else:
      current=S[25-i]
  if not done:
    print(-1)
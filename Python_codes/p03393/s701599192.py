s = input()
abc = [chr(i) for i in range(ord('a'), ord('z')+1)]

if len(s) == 26:
  for i in range(24, -1, -1):
    cand = list(s[i+1:])
    cand.sort()
    for c in cand:
      if ord(c) > ord(s[i]):
        print(s[:i] + c)
        exit()
  print(-1)
else:
  for l in abc:
    if l not in s:
      print(s + l)
      exit()
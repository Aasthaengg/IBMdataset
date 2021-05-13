S = input()

flag = [0]*26

if S == 'zyxwvutsrqponmlkjihgfedcba':
  print(-1)
  exit()

if len(S) < 26:
  for s in S:
    flag[ord(s)-ord('a')] = 1
  print(S + chr(flag.index(0)+ord('a')))
  
else:
  a = 0
  for i in range(len(S)-1,-1,-1):
    if a < ord(S[i]):
      flag[ord(S[i])-ord('a')] = 1
      a = ord(S[i])
    else:
      print(S[:i]+chr(flag[ord(S[i])-ord('a'):].index(1)+ord(S[i])))
      break
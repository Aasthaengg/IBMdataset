S=input()
A=[chr(ord('a') + i) for i in range(26)]
if S=='zyxwvutsrqponmlkjihgfedcba':
  print(-1)
else:
  if len(S)<26:
    for i in A:
      if str(i) not in S:
        print(S+str(i))
        exit()
  else:
    for i in range(24,-1,-1):
      for j in range(25,i,-1):
        if S[i] < S[j]:
          print(S[:i]+S[j])
          exit()
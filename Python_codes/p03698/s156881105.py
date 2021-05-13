s=input()
S=[s[i] for i in range(len(s))]
c=1
for i in range(len(S)-1):
  if S[i] in S[i+1:]:
    c=0
    break
if c==1:
  print('yes')
else:
  print('no')
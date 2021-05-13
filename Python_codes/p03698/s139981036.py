S=input()
S=S+'0'
S=sorted(S)
for i in range(len(S)-1):
  if S[i]==S[i+1]:
    print('no')
    exit()
print('yes')
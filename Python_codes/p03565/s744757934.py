S=input()
T=input()
if len(S)<len(T):
  print('UNRESTORABLE')
  exit()
else:
  list=[]
  for i in range(len(S)-len(T)+1):
    count=0
    for j in range(len(T)):
      if S[i+j]==T[j] or S[i+j]=='?':
        count+=1
    if count==len(T):
      SS=S[:i]+T+S[i+len(T):]
      for m in range(len(S)):
        if SS[m]=='?':
          SS=SS[:m]+'a'+SS[m+1:]
      list.append(SS)
list.sort()
if list==[]:
  print('UNRESTORABLE')
else:
  print(list[0])
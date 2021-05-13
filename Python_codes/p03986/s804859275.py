S=input()
score=0
maxscore=0
for i in range(len(S)):
  if S[i]=='T':
    score+=1
    maxscore=max(maxscore,score)
  else:
    score-=1
print(2*maxscore)
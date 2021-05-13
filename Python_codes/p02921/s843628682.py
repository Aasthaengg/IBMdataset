stdin = open(0).read().split('\n')
S = stdin[0]
T = stdin[1]
day=0
if S[0]==T[0]:day+=1
if S[1]==T[1]:day+=1
if S[2]==T[2]:day+=1
print(day)
N,K=map(int,input().split())
S=input()
S='.'+S
S=S+'.'
P=0
for i in range(N):
  if S[i+1]=='L':
    if S[i]=='L':
      P+=1
  else:
    if S[i+2]=='R':
      P+=1
print(min(N-1,P+K*2))
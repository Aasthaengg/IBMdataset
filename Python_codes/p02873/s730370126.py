S = input()
n = [0]*(len(S)+1)

if S[0]=='<':
    n[0]==0
if S[-1]=='>':
    n[-1]==0
for i in range(1,len(S)):
    if S[i-1]=='<' and S[i]=='<':
        n[i] = n[i-1]+1
        n[i+1]=n[i]+1
    elif S[i-1]=='>' and S[i]=='<':
        n[i] = 0
        n[i+1]=1
        
for i in range(len(S)-1,-1,-1):
    if S[i]=='>':
        n[i]=max(n[i],n[i+1]+1)
        
print(sum(n))
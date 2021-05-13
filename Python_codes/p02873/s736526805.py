S = input()
n = [0]*(len(S)+1)

if S[0]=='<':
    n[0]==0
for i in range(0,len(S)):
    if S[i]=='>':
        n[i+1]=0
    else:
        n[i+1]=n[i]+1
        
for i in range(len(S)-1,-1,-1):
    if S[i]=='>':
        n[i]=max(n[i],n[i+1]+1)
        
print(sum(n))
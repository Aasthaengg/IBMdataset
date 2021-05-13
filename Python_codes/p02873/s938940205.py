import sys
def S(): return sys.stdin.readline().rstrip()
S = S()
seq = [0]*(len(S)+1)
for i in range(len(S)):
    if S[i]=='<':
        seq[i+1] = seq[i]+1
for j in range(len(S)-1,-1,-1):
    if S[j]=='>':
        seq[j] = max(seq[j],seq[j+1]+1)
print(sum(seq))

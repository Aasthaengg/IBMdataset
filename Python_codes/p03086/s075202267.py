S=list(input())
a=0
b=[0]
for i in range(len(S)-1):
    if S[i]=='A' or S[i]=='C' or S[i]=='G' or S[i]=='T':
        b[len(b)-1]+=1
    if (S[i]=='A' or S[i]=='C' or S[i]=='G' or S[i]=='T') and (S[i+1]!='A' and S[i+1]!='C' and S[i+1]!='G' and S[i+1]!='T'):
        b.append(0)
if S[len(S)-1]=='A' or S[len(S)-1]=='C' or S[len(S)-1]=='G' or S[len(S)-1]=='T':
    b[len(b)-1]+=1
print(max(b))          
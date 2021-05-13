S=input()
cnt=0
lis=[0]
for i in range(len(S)):
    if S[i]=='A'or S[i]=='C' or S[i]=='G' or S[i]=='T':
        cnt+=1
        lis.append(cnt)
    else:
        cnt=0
print(max(lis))
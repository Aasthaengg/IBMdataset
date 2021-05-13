s=input()
S=list(s)
k=len(S)
count=0
for i in range(k):
    if S[i]=='o':
        count+=1
    else:
        continue
if 15-k+count>7:
    print('YES')
else:
    print('NO')
u=str(input())
S=u.replace(' ','z')
A=[]
for i in range(len(S)+1):
    for j in range(len(S)+1):
        if i<=j:
            A.append(S.replace(S[i-1:j],'',1))
if 'keyence' in A:
    print('YES')
else:
    print('NO')
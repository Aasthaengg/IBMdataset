S=list(input())
a=0
for i in range(len(S)):
    if S[i]=='x':
        a+=1
if a<=7:
    print('YES')
else:
    print('NO')
import re
S = input()

goal = 'AKIHABARA'
li = [0,4,6,8]
flag = False
N=4
for i in range(1<<N):
    exli = []
    s = ''
    for j in range(N):
        if((i>>j&1)==1):
            exli.append(li[j])
    for ind,c in enumerate(goal):
        if(ind not in exli):
            s+=c
    if(s==S):
        flag = True
        break
if(flag):
    print('YES')
else:
    print('NO')
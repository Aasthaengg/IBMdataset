N,M = map(int,input().split())
S = {}
Answer = 2
for i in range(M):
    s,c = map(int,input().split())
    s = str(s)
    if s not in S:
        S[s] = str(c)
    else:
        if str(c) != S[s]:
            Answer = -1
            break
        else:
            continue
if N >= 2:
    if '1' in S:
        if N== 2 and S['1'] == '0':
            Answer = -1
        elif N == 3 and S['1'] == '0':
            Answer = -1
if Answer != -1:
    if '1' not in S and N >=2:
        Answer = '1'
    elif '1' not in S and N == 1:
        Answer ='0'
    else:
        Answer = S['1']
    for i in range(1,N):
        stri = str(i+1)
        if stri in S:
            Answer = Answer + S[stri]
        else:
            Answer = Answer + '0'
print(int(Answer))
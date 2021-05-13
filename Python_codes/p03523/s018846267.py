#A - AKIBA △
S = input()
S = list(S)

SS = []
for p in S:#Aを追加する空白を作る
    SS.append('')
    SS.append(p)
SS.append('')


result = 'NO'
if len(S) <= 9 and 'K' in S and 'I' in S and 'H' in S and 'B' in S and 'R' in S:
    for i in range(1<<(len(SS))):
        SSS = SS.copy()
        for j in range(len(SS)):
            mask = 1 << j
            if mask & i != 0:#処理を行う
                if SSS[j] == '':
                    SSS[j] = 'A'
        for k in SSS:
            if k == '':
                SSS.remove('')
        if SSS == ['A','K','I','H','A','B','A','R','A']:
            result = 'YES'
print(result)
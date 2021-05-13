S = input()
M = {'a':0,'b':0,'c':0}
for s in S:
    M[s] += 1
L = sorted(M.values(),key=lambda x: -x)
if len(L) == 1:
    if L[0] == 1:
        print('YES')
    else:
        print('NO')
elif len(L) == 2:
    print('NO')
else:
    if L[0] - L[2] > 1:
        print('NO')
    else:
        print('YES')
import itertools
def S(): return input()
S = S()
AKIBA_list = list(itertools.accumulate('AKIHABARA'))
for i,x in enumerate(AKIBA_list):
    if S[:i+1]==x:
        continue
    S = S[:i]+'A'+S[i:]
    if S[:i+1]==x:
        continue
    print('NO')
    break
else:
    if S=='AKIHABARA':
        print('YES')
    else:
        print('NO')

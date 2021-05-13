import itertools,sys
def S(): return sys.stdin.readline().rstrip()
S = S()
count = 0
for i,j in itertools.combinations_with_replacement(range(len(S)+1),2):
    if S[:i]+S[j:]=='keyence':
        print('YES')
        break
else:
    print('NO')

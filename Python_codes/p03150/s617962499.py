import itertools,sys
def S(): return sys.stdin.readline().rstrip()
S = S()
for i,j in itertools.combinations(range(len(S)+2),2):
    if S[:i]+S[j-1:]=='keyence':
        print('YES')
        break
else:
    print('NO')

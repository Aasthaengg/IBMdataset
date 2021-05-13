# dfs
import sys
sys.setrecursionlimit(10**6)

C = ['dream', 'dreamer', 'erase', 'eraser']
S = input()
L = len(S)


def dfs(x, l):
    if l == L:
        return True
    elif l > L:
        return False

    match = S[l:l+7]
    for c in C:
        if match.find(c) == 0:
            if dfs(c, l+len(c)):
                return True
    return False


print('YES' if dfs('', 0) else 'NO')

# dfs
import sys
sys.setrecursionlimit(10**6)

C = ['dream', 'dreamer', 'erase', 'eraser']
S = input()
L = len(S)

def dfs(l):
    if l == L:
        return True
    elif l > L:
        return False

    for c in C:
        if S.find(c, l, l+7) == l:
            if dfs(l+len(c)):
                return True
    return False

print('YES' if dfs(0) else 'NO')

from collections import *

def dfs(now):
    if len(now)==N:
        print(''.join(now))
        return

    for i in range(ord(max(now))-ord('a')+2):
        now.append(alpha[i])
        dfs(now)
        now.pop()

N = int(input())
alpha = 'abcdefghijklmnopqrstuvwxyz'
dfs(deque(['a']))
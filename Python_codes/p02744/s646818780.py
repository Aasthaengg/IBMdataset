import sys
sys.setrecursionlimit(10**7)
n = int(input())
ls = []


def dfs(s):
    if len(s) == n:
        ls.append(s)
        return 0
    else:
        for x in map(chr, range(97, ord(max(s))+2)):
            dfs(s+x)


dfs("a")
ls.sort()
for x in ls:
    print(x)

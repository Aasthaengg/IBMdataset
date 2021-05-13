import sys
sys.setrecursionlimit(10**7)


def dfs(s, max_ctoi, n):
    global ans
    if len(s) == n:
        ans.append(s)
        return
    else:
        for i in range(max_ctoi+1):
            if i == max_ctoi:
                dfs(s+chr(ord("a")+i), max_ctoi+1, N)
            else:
                dfs(s+chr(ord("a")+i), max_ctoi, N)


ans = []
N = int(input())
dfs("", 0, N)
ans.sort()
for a in ans:
    print(a)

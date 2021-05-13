# カンニングしました。。。。。。。。

def dfs(s: str, m: int):
    global n
    if len(s) == n:
        print(s)
    else:
        for c in range(ord('a'), m + 1):
            dfs(s + chr(c), m + 1 if c == m else m)


n = int(input())
dfs('', ord('a'))

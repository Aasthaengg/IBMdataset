# https://atcoder.jp/contests/panasonic2020/tasks/panasonic2020_d

n = int(input())

def dfs(s, mx, path):
    if n == len(s):
        path.append(s)
        return
    for i in range(ord('a'), mx + 1):
        if i == mx:
            dfs(s + chr(i), mx + 1, path)
        else:
            dfs(s + chr(i), mx, path)

path = []
dfs('', ord('a'), path)
path.sort()
for ans in path:
    print(ans)
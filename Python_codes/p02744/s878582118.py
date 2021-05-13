n = int(input())
ans = []

l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


def dfs(s):
    if len(s) >= n:
        return
    f = False
    for x in l:
        if x in s:
            ans.append(s + x)
            dfs(s + x)
        else:
            if f:
                return
            f = True
            ans.append(s + x)
            dfs(s + x)


dfs('')

ans.sort()
for x in ans:
    if len(x)==n:
        print(x)

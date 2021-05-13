def dfs(i, f):
    if i == len(s) - 1:
        if eval(f) == 7:
            print(f + '=7')
            exit()
    else:
        dfs(i+1, f + '+' + s[i+1])
        dfs(i+1, f + '-' + s[i+1])
s = list(input())
dfs(0, s[0])
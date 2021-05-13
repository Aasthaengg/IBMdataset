def dfs(i,sum1,sum2):
    global ans
    if i == 4 and sum1 != 7:
        return 0
    elif i == 4 and sum1 == 7:
        ans = sum2 + "=7"
        return 0
    else:
        dfs(i + 1,sum1 + int(s[i]),sum2 + "+" + s[i])
        dfs(i + 1, sum1 - int(s[i]), sum2 + "-" + s[i])

s = input()
ans = ""
dfs(1,int(s[0]),s[0])
print(ans)

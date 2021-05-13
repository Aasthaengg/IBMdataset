L = list(map(int, list(input())))

def dfs(ans, index, cnt):
    if index == 0:
        return dfs(ans + str(L[index]), index + 1, cnt + L[index])
    if index == 4:
        if cnt == 7:
            return ans + '=7'
        else:
            return False
    ans1 = dfs(ans + '+' + str(L[index]), index+1, cnt + L[index])
    ans2 = dfs(ans + '-' + str(L[index]), index+1, cnt - L[index])
    if ans1:
        return ans1
    if ans2:
        return ans2
    return False

ans = dfs('', 0, 0)
print(ans)
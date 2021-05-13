n, a, b, c = map(int, input().split())
l = [int(input()) for _ in range(n)]
INF = 10**9


def dfs(pos, a_tmp, b_tmp, c_tmp):
    if pos == n:
        if min(a_tmp, b_tmp, c_tmp) > 0:
            return abs(a-a_tmp)+abs(b-b_tmp)+abs(c-c_tmp)-30
        else:
            return INF
    res0 = dfs(pos+1, a_tmp, b_tmp, c_tmp)
    res1 = dfs(pos+1, a_tmp+l[pos], b_tmp, c_tmp)+10
    res2 = dfs(pos+1, a_tmp, b_tmp+l[pos], c_tmp)+10
    res3 = dfs(pos+1, a_tmp, b_tmp, c_tmp+l[pos])+10
    return min(res0, res1, res2, res3)


print(dfs(0, 0, 0, 0))

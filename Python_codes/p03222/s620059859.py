h, w, k = map(int, input().split())

mod = 10 ** 9 + 7

def dfs(idx, used):
    if idx == w - 1:
        return [[]]

    ret = dfs(idx + 1, False)
    if used == False:
        ret2 = dfs(idx + 1, True)
        for l in ret2:
            ret.append(l + [idx])
    return ret

combs = dfs(0, 0)

dp = [0] * w
dp[0] = 1
for i in range(h):
    dp_new = [0] * w
    for bars in combs:
        used = set()
        for start in bars:
            dp_new[start] += dp[start + 1]
            dp_new[start + 1] += dp[start]

            used.add(start)
            used.add(start + 1)

        for i in range(w):
            if i not in used:
                dp_new[i] += dp[i]

    dp = [x % mod for x in dp_new]

print(dp[k-1])

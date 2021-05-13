n = input()
s = []
for c in n:
    s.append(int(c))
s.reverse()
l = len(s)
INF = 1000000000


def get_next(c):
    ret = [
        [INF, INF],
        [INF, INF],
    ]
    # for a in range(10):
    #     for b in range(10):
    #         if a - b == c:
    #             ret[0][0] = min(ret[0][0], a + b)
    #         if 10 + a - b == c:
    #             ret[0][1] = min(ret[0][1], a + b)
    #         if a - 1 - b == c:
    #             ret[1][0] = min(ret[1][0], a + b)
    #         if 10 + a - 1 - b == c:
    #             ret[1][1] = min(ret[1][1], a + b)
    for b in range(10):
        a = c + b
        if 0 <= a < 10:
            ret[0][0] = min(ret[0][0], a+b)
        a = c + b - 10
        if 0 <= a < 10:
            ret[0][1] = min(ret[0][1], a+b)
        a = c + b + 1
        if 0 <= a < 10:
            ret[1][0] = min(ret[1][0], a + b)
        a = c + b - 10 + 1
        if 0 <= a < 10:
            ret[1][1] = min(ret[1][1], a + b)
    return ret


dp = [[0 for _ in range(l+1)] for _ in range(2)]

dp[1][0] = INF

for i, c in enumerate(s):
    next_step = get_next(c)
    dp[0][i+1] = min(dp[0][i]+next_step[0][0], dp[1][i]+next_step[1][0])
    dp[1][i+1] = min(dp[0][i]+next_step[0][1], dp[1][i]+next_step[1][1])

print(min(dp[0][l], dp[1][l]+1))
# print(dp)
n, k = map(int, input().split())
a = list(map(int, input().split()))

dp = [[None] * (k + 1) for _ in range(2)]
# def dfs(at=k, taro=True):
#     if dp[taro][at]:
#         return dp[taro][at]
#
#     if at == 0:
#         r = True ^ taro # taro lose -> False
#         dp[taro][at] = r
#         return r
#
#     results = []
#     for i in range(n):
#         if at >= a[i]:
#             results.append(dfs(at - a[i], not taro))
#
#     if not results:
#         r = True ^ taro
#         dp[taro][at] = r
#         return r
#     r = (any if taro else all)(results)
#     dp[taro][at] = r
#     return r

for at in range(k + 1):
    for taro in range(2):
        if at == 0:
            dp[taro][at] = not taro
            continue
        results = []
        for i in range(n):
            if at >= a[i]:
                results.append(dp[not taro][at - a[i]])

        if not results:
            dp[taro][at] = not taro
            continue
        dp[taro][at] = (any if taro else all)(results)
print('First' if dp[True][k] else 'Second')

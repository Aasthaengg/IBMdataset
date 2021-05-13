S = '_' + input()
### dp[i文字目まで読んだ][直前に読んだ文字] = 分割数
dp = []
for _ in range(len(S) + 1):
    dp += [{}]
if len(S) == 2:
    print(1)
else:
    dp[2][S[1:2]] = 1
    dp[3][S[1:3]] = 1
    index = 2
    while index < len(S):
        for k, v in dp[index].items():
            if index + 1 <= len(S):
                s = S[index: index + 1]
                # print(f"index:{index} k:{k} v:{v} s:{s}", file=sys.stderr)
                if s != k:
                    if not s in dp[index + 1]:
                        dp[index + 1][s] = v + 1
                    elif s in dp[index + 1] and dp[index + 1][s] < v + 1:
                        dp[index + 1][s] = v + 1
            if index + 2 <= len(S):
                s = S[index: index + 2]
                if s != k:
                    if not s in dp[index + 2]:
                        dp[index + 2][s] = v + 1
                    elif s in dp[index + 2] and dp[index + 2][s] < v + 1:
                        dp[index + 2][s] = v + 1
        index += 1
    # print(f'len:{len(S)} dp:{dp}', file=sys.stderr)
    print(max([v for k, v in dp[-1].items()]))
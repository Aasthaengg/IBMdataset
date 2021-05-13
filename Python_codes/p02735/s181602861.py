#!/usr/bin/env python3
import sys


def solve(H: int, W: int, s: "List[str]"):
    dp = [[0 for w in range(W)] for h in range(H)] # dp[h][w]はh,wに達するための回数
    if s[0][0] == '#':
        dp[0][0] = 1

    for w in range(W-1): # 0行目について
        if s[0][w+1] == '.': # 移動先が白だったら特に変わりなし
            dp[0][w+1] = dp[0][w]
        elif s[0][w] == '.' and s[0][w+1] == '#': # 移動元が白で先が黒ならば、新しく施行1回追加
            dp[0][w+1] = dp[0][w] + 1
        elif s[0][w] == '#' and s[0][w+1] == '#': # 移動元も先も黒だったとしたら、試行回数は変わらない
            dp[0][w+1] = dp[0][w]

    for h in range(H-1): # 1列目について
        if s[h+1][0] == '.':
            dp[h+1][0] = dp[h][0]
        elif s[h][0] == '.' and s[h+1][0] == '#':
            dp[h+1][0] = dp[h][0] + 1
        elif s[h][0] == '#' and s[h+1][0] == '#':
            dp[h+1][0] = dp[h][0]

    for h in range(1, H):
        for w in range(W-1):
            if s[h][w+1] == '.':
                dp[h][w+1] = min(dp[h][w], dp[h-1][w+1])
            elif s[h][w] == '.' and s[h][w+1] == '#':
                if s[h-1][w+1] == '.':
                    dp[h][w+1] = min(dp[h][w]+1, dp[h-1][w+1]+1)
                elif s[h-1][w+1] == '#':
                    dp[h][w+1] = min(dp[h][w]+1, dp[h-1][w+1])
            elif s[h][w] == '#' and s[h][w+1] == '#':
                if s[h-1][w+1] == '.':
                    dp[h][w+1] = min(dp[h][w], dp[h-1][w+1]+1)
                elif s[h-1][w+1] == '#':
                    dp[h][w+1] = min(dp[h][w], dp[h-1][w+1])
    print(dp[H-1][W-1])
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    s = [next(tokens) for _ in range(H)]  # type: "List[str]"
    solve(H, W, s)

if __name__ == '__main__':
    main()
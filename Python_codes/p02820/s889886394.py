# K個の独立した問題として考える

N, K = map(int, input().split())
RSP = list(map(int, input().split()))
T = input()

def is_win(me, other):
    if me == 0 and other == 1:
        return True
    elif me == 1 and other == 2:
        return True
    elif me == 2 and other == 0:
        return True
    return False

def char_to_num(s):
    if s == "r":
        return 0
    elif s == "s":
        return 1
    else:
        return 2

# dp[i][j] = i回目のじゃんけんでjを出して取れる最大の点数([i%K]ごとに独立)
dp = [[-1 for j in range(3)] for i in range(N+1)]
dp[0] = [0, 0, 0]
for i in range(1, N+1):
    t = char_to_num(T[i-1])
    if i <= K:
        for j in range(3):
            dp[i][j] = is_win(j, t)*RSP[j]
    else:    
        for j in range(3):
            dp[i][j] = max(
                [dp[i-K][k] + is_win(j, t)*RSP[j] for k in range(3) if j != k]
            )

# print(dp)

r = sum(map(max, dp[-K:]))
print(r)
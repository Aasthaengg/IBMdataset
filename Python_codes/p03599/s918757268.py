import heapq

def main():
    A, B, C, D, E, F = map(int, input().split())
    dp = {0: 0}
    mt, ms = 100 * A, 0
    for i in range(1, F + 1):
        s = -1
        if i - 100 * A in dp:
            s = max(s, dp[i - 100 * A])
        if i - 100 * B in dp:
            s = max(s, dp[i - 100 * B])
        if i - C in dp:
            if dp[i - C] + C <= E * (i - C - dp[i - C]) // 100:
                s = max(s, dp[i - C] + C)
        if i - D in dp:
            if dp[i - D] + D <= E * (i - D - dp[i - D]) // 100:
                s = max(s, dp[i - D] + D)
        if s >= 0:
            if 100 * s * mt > 100 * ms * i:
                mt, ms = i, s
            dp[i] = s
    return mt, ms 

print(*main())

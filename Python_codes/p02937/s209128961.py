def next(str):
    N = len(str)
    nxt = [[N] * 26 for i in range(N + 1)]
    for i in range(N - 1, -1, -1):
        for j in range(26):
            nxt[i][j] = nxt[i + 1][j]
        nxt[i][ord(str[i]) - ord('a')] = i
    return nxt

def solve():
    S = input()
    T = input()
    N = len(S)
    M = 2 * N
    S += S
    nxt = next(S)
    ans = -1
    for c in T:
        i = ans % N
        pos = ord(c) - ord('a')
        if nxt[i + 1][pos] == M:
            return -1
        ans += nxt[i + 1][pos] - i
    return ans + 1

print(solve())

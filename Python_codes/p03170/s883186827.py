# At DP K
def solve(K, A):
    dp = [ False ] * (K + 1)
    # dp[i] - true if current player wins if there are i stones remaining
    for stones in range(K + 1):
        for w in A:
            if stones >= w: # there must be more stones than we are removing
                if not dp[stones - w]: # does the opponent win after we remove `w` stones?
                    dp[stones] = True # then this player does win
    return "First" if dp[K] else "Second"

assert solve(7, [2, 3]) == "First"
assert solve(5, [2, 3]) == "Second"
assert solve(4, [2, 3]) == "First"
assert solve(20, [1, 2, 3]) == "Second"
assert solve(21, [1, 2, 3]) == "First"
assert solve(100000, [1]) == "Second"

n, k = map(int, input().split())
A = list(map(int, input().split()))

ans = solve(k, A)
print(ans)


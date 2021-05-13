import collections
def dfs(i, cumul, cc, k, s): return (cumul if k == 0 else 0) if (i == len(s) or k == 0) else (dfs(i+1,  cumul * cc[s[i]], cc,k - 1, s) +dfs(i+1,  cumul, cc, k, s))
print dfs(0,  1 , collections.Counter([raw_input()[0] for _ in range(int(raw_input()))]), 3, 'MARCH')

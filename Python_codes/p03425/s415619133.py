def solve():
    from collections import defaultdict
    from itertools import combinations
    n = int(input())
    d = defaultdict(int)
    for i in range(n):
        s = input()
        d[s[0]] += 1
    ans = 0
    for x, y, z in combinations(["M", "A", "R", "C", "H"], 3):
        ans += d[x] * d[y] * d[z]
    print(ans)
    return


solve()

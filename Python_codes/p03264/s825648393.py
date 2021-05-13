from itertools import combinations

# input
K = int(input())

# check
cnt = len(
    [
        1
        for c in list(combinations(list(range(1, K + 1)), 2))
        if (c[0] + c[1]) % 2 == 1
    ]
)

print(cnt)

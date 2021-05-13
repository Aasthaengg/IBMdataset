import itertools


h, w, k = map(int, input().split())

if w == 1:
    print(1)
    exit()

mod = 10**9 + 7
path = [[i, i+1] for i in range(w-1)]
DP = [[0]*(h+1) for _ in range(w)]
DP[0][0] = 1

for height in range(h):
    for pos in range(w):
        down_unable = {pos}
        left_unable = {pos-1, pos}
        right_unable = {pos, pos+1}

        down_count = 1
        left_count = 1
        right_count = 1
        for pick in range(1, 1 + w//2):
            all_pattern = list(itertools.combinations(path, pick))

            for pattern in all_pattern:
                check = set()
                possible = True
                for a, b in pattern:
                    if check & {a, b}:
                        possible = False
                        break
                    check |= {a, b}
                if not possible:
                    continue
                if not check & down_unable:
                    down_count += 1
                if not check & left_unable:
                    left_count += 1
                if not check & right_unable:
                    right_count += 1

        if pos == 0:
            DP[pos][height+1] += DP[pos][height] * down_count % mod
            DP[pos+1][height+1] += DP[pos][height] * right_count % mod

        elif pos == w-1:
            DP[pos][height+1] += DP[pos][height] * down_count % mod
            DP[pos-1][height+1] += DP[pos][height] * left_count % mod
        else:
            DP[pos][height+1] += DP[pos][height] * down_count % mod
            DP[pos+1][height+1] += DP[pos][height] * right_count % mod
            DP[pos-1][height+1] += DP[pos][height] * left_count % mod

print(DP[k-1][h] % mod)

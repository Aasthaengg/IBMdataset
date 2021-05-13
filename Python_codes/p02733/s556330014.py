h, w, k = (int(x) for x in input().split())
S = [input() for _ in range(h)]

ans = 10**18
for bit in range(1<<(h - 1)):
    segment = [0] * h
    seg_label = 0
    for i in range(h - 1):
        if bit & (1<<i):
            seg_label += 1
        segment[i + 1] = seg_label
    n = max(segment) + 1

    count = n - 1
    k_count = [0] * n
    for j in range(w):
        tmp_count = [0] * n
        for i in range(h):
            k_count[segment[i]] += int(S[i][j])
            tmp_count[segment[i]] += int(S[i][j])
            if k_count[segment[i]] > k:
                count += 1
                for seg in range(n):
                    k_count[seg] = tmp_count[seg]

    ans = min(ans, count)

print(ans)

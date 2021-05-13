def compress(S):
    res = []
    prev = "aa"
    for c in S:
        if c != prev:
            res.append([c, 1])
        else:
            res[-1][1] += 1
        prev = c
    return res


N, K = map(int, input().split())
S = list(map(int, input()))
S_comp = compress(S)
M = len(S_comp)
ans = 0
total = 0
right = 0
zero_chunks_cnt = 0
for left in range(M):
    while right < M and zero_chunks_cnt + 1 - S_comp[right][0] <= K:
        zero_chunks_cnt += 1 - S_comp[right][0]
        total += S_comp[right][1]
        right += 1
    ans = max(ans, total)
    if right == left:
        right += 1
    else:
        zero_chunks_cnt -= 1 - S_comp[left][0]
        total -= S_comp[left][1]
print(ans)

def run_length_compress(S):
    res = [[S[0], 1]]
    for c in S[1:]:
        if c == res[-1][0]:
            res[-1][1] += 1
        else:
            res.append([c, 1])
    return res


def solve():
    S = input()
    N = len(S)
    K = int(input())
    T = run_length_compress(S)
    if T[0][1] == N:
        return N * K // 2
    ans = sum(l // 2 for _, l in T) * K
    if T[0][0] == T[-1][0]:
        head_cnt, tail_cnt = T[0][1], T[-1][1]
        tmp = (head_cnt + tail_cnt) // 2 - head_cnt // 2 - tail_cnt // 2
        ans += tmp * (K - 1)
    return ans


print(solve())

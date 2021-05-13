def run_length_compress(S):
    res = [[S[0], 1]]
    for c in S[1:]:
        if c == res[-1][0]:
            res[-1][1] += 1
        else:
            res.append([c, 1])
    return res


S = input()
N = len(S)
K = int(input())
T = run_length_compress(S)
if T[0][1] == N:
    print(N * K // 2)
    exit()
ans = sum(l // 2 for _, l in T) * K
if T[0][0] == T[-1][0]:
    head, tail = T[0][1], T[-1][1]
    ans += ((head + tail) // 2 - head // 2 - tail // 2) * (K - 1)
print(ans)

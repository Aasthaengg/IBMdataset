from collections import Counter
N = int(input())
P = list(tuple(map(int, input().split())) for _ in range(N))
P = sorted(P)

p_q_cand = []
for i in range(N):
    for j in range(i+1, N):
        diff_p = P[j][0]-P[i][0]
        diff_q = P[j][1]-P[i][1]
        p_q_cand.append((diff_p, diff_q))

if N == 1:
    print(1)
else:
    C = Counter(p_q_cand)
    ans = float('inf')
    for v, c in C.items():
        p = v[0]
        q = v[1]
        tmp = 0
        used = set()
        for a, b in sorted(list(P), key=lambda x: (x[0], x[1])):
            if (a-p, b-q) not in used:
                tmp += 1
            used.add((a, b))
        ans = min(ans, tmp)
    print(ans)

N, M, Q = map(int, input().split())

rules = []
for _ in range(Q):
    a, b, c, d = map(int, input().split())
    a, b = a-1, b-1
    rules.append((a, b, c, d))

def gen():
    seq = [[1]]
    for _ in range(N-1):
        new_seq = []
        for prefix in seq:
            for i in range(prefix[-1], M+1):
                new_seq.append(prefix+[i])
        seq = new_seq
    return seq

ans = 0
for A in gen():
    cand = 0
    for a, b, c, d in rules:
        if A[b]-A[a] == c:
            cand += d
    ans = max(ans, cand)
print(ans)
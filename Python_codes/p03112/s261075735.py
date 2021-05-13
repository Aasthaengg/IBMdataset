A, B, Q = map(int, input().split())
S = [int(input()) for _ in range(A)]
T = [int(input()) for _ in range(B)]
query, X = [], {}

for i in range(Q):
    q = int(input())
    query.append(q)
    X[q] = i
query.sort()

near_s = [0 for _ in range(Q)]
near_t = [0 for _ in range(Q)]
j = 0
while j < Q and query[j] < S[0]:
    near_s[j] = [0, S[0]]
    j += 1    
for i in range(A-1):
    while j < Q and S[i] < query[j] < S[i+1]:
        near_s[j] = [S[i], S[i+1]]
        j += 1
near_s = near_s[:j] + [[S[A-1],0] for _ in range(Q-j)]

j = 0
while j < Q and query[j] < T[0]:
    near_t[j] = [0, T[0]]
    j += 1
for i in range(B-1):
    while j < Q and T[i] < query[j] < T[i+1]:
        near_t[j] = [T[i], T[i+1]]
        j += 1
near_t = near_t[:j] + [[T[B-1],0] for _ in range(Q-j)]

ans = [0]*Q
for i in range(Q):
    q, s0, s1, t0, t1 = query[i], near_s[i][0], near_s[i][1], near_t[i][0], near_t[i][1]
    l1 = q - min(s0, t0)
    l2 = max(s1, t1) - q
    l3 = s1 - t0 + min(s1 - q, q - t0)
    l4 = t1 - s0 + min(t1 - q, q - s0)
    if s0 == 0:
        l1, l4 = float('inf'), float('inf')
    if s1 == 0:
        l2, l3 = float('inf'), float('inf')
    if t0 == 0:
        l1, l3 = float('inf'), float('inf')
    if t1 == 0:
        l2, l4 = float('inf'), float('inf')
    ans[X[q]] = min(l1, l2, l3, l4)

for a in ans:
    print(a)
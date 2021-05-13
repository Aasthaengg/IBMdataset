import bisect

A, B, Q = map(int, input().split())
K = []
T = []
for i in range(A):
    K.append(int(input()))
for j in range(B):
    T.append(int(input()))
K.sort()
T.sort()
l_1 = len(K)
l_2 = len(T)

Ans = []
for i in range(Q):
    c = int(input())
    p = bisect.bisect_right(K, c)
    if p >= l_1:
        p -= 1
    dis_1 = abs(c - K[p-1])
    dis_2 = abs(c - K[p])
    q_1 = bisect.bisect_right(T, K[p-1])
    q_2 = bisect.bisect_right(T, K[p])
    if q_1 >= l_2:
        q_1 -= 1
    if q_2 >= l_2:
        q_2 -= 1
    result_1 = min([dis_1 + abs(K[p-1] - T[q_1-1]), dis_1 + abs(K[p-1] - T[q_1]), dis_2 + abs(K[p] - T[q_2-1]), dis_2 + abs(K[p] - T[q_2])])

    p = bisect.bisect_right(T, c)
    if p >= l_2:
        p -= 1
    dis_1 = abs(c - T[p-1])
    dis_2 = abs(c - T[p])
    q_1 = bisect.bisect_right(K, T[p-1])
    q_2 = bisect.bisect_right(K, T[p])
    if q_1 >= l_1:
        q_1 -= 1
    if q_2 >= l_1:
        q_2 -= 1
    result_2 = min([dis_1 + abs(T[p-1] - K[q_1-1]), dis_1 + abs(T[p-1] - K[q_1]), dis_2 + abs(T[p] - K[q_2-1]), dis_2 + abs(T[p] - K[q_2])])
    Ans.append(min(result_1, result_2))

for i in Ans:
    print(i)
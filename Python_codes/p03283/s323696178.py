from collections import defaultdict
N, M, Q = map(int, input().split())
T = []
for i in range(M):
    L, R = map(int, input().split())
    T.append([L, R, 0])
for i in range(Q):
    L, R = map(int, input().split())
    T.append([L, R, 1, i])

Ans = [0]*Q
d = defaultdict(int)
T = sorted(T, key=lambda x: (x[1], x[2]))
for i in range(len(T)):
    result = 0
    if T[i][2] == 0:
        d[T[i][0]] += 1
    else:
        for j in range(T[i][0], T[i][1]+1):
            result += d[j]
        Ans[T[i][3]] = result

for i in Ans:
    print(i)
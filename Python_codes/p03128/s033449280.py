import sys
input = sys.stdin.buffer.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
Need = [-1, 2, 5, 5, 4, 5, 6, 3, 7, 6]
Usable = {}
for a in A:
    if Need[a] in Usable:
        for key, value in Usable.items():
            if Need[a] == key and a > value:
                Usable[key] = a
    else:
        Usable[Need[a]] = a
Num = [-1] * (N + 1)
Num[0] = 0
for i in range(1, N+1):
    for u, v in Usable.items():
        if i < u:
            continue
        if Num[i - u] >= 0:
            if Num[i - u] == 0:
                Num[i] = max(v, Num[i])
            elif Num[i] < Num[i - u] * 10 + v:
                Num[i] = Num[i - u] * 10 + v

print(Num[N])
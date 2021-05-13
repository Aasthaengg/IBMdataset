from collections import defaultdict
d = defaultdict(int)
N = int(input())
for i in range(1, N+1):
    K = i
    for j in range(2, N+1):
        if K >= j:
            while(K % j == 0):
                d[j] += 1
                K = K//j
T = defaultdict(int)
for k, v in d.items():
    if v >= 2:
        T[2] += 1
    if v >= 4:
        T[4] += 1
    if v >= 14:
        T[14] += 1
    if v >= 24:
        T[24] += 1
    if v >= 74:
        T[74] += 1

ans = 0
ans += T[4]*(T[4]-1)*(T[2]-2)//2
ans += T[14]*(T[4]-1)
ans += (T[2]-1)*T[24]
ans += T[74]
print(ans)
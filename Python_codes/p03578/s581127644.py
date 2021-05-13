from collections import Counter
N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

Dc = Counter(D)
Tc = Counter(T)

if (N < M):
    print('NO')
    exit()

for i, c in Tc.items():
    if (Dc[i] < c):
        print('NO')
        exit()
    else:
        continue

print('YES')

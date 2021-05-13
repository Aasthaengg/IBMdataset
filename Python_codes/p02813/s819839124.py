N = int(input())
P = ''.join(map(str, list(map(int, input().split()))))
Q = ''.join(map(str, list(map(int, input().split()))))
import itertools

T = [''.join(map(str, a)) for a in sorted(list(itertools.permutations(range(1, N + 1))))]

P_i = 0
Q_i = 0
for i, t in enumerate(T):
    if t == P:
        P_i = i
    if t == Q:
        Q_i = i
ans = abs(P_i - Q_i)
print(ans)

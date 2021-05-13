from collections import Counter, defaultdict
S = input()
T = input()

S_count = Counter(S)
T_count = Counter(T)

d_S = defaultdict(int)
d_T = defaultdict(int)
for i in range(len(S)):
    d_S[S_count[S[i]]] += 1
    d_T[T_count[T[i]]] += 1

if (d_S == d_T):
    print('Yes')
else:
    print('No')

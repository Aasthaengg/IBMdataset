N = int(input())
L = list(input() for i in range(N))
M = int(input())
T = list(input() for i in range(M))

Li = []
for i in set(L):
    if i not in T:
        K = 0
    else:
        K = T.count(i)
    Li.append(L.count(i) - K)

print(max(Li) if max(Li)>0 else 0)

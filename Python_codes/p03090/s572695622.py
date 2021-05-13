N = int(input())

def graph(N):
    if N % 2 != 0:
        E = graph(N - 1)
        E.extend((i, N) for i in range(1, N))
    else:
        E = [(i, j) for i in range(1, N)
                    for j in range(i + 1, N + 1) if i + j != N + 1]
    return E

E = graph(N)
print(len(E))
print('\n'.join(' '.join(map(str, e)) for e in E))
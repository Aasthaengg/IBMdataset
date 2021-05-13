ri = lambda: map(int, input().split())

N, M = ri()
H = list(ri())
T = [0]*N
for _ in range(M):
    a, b = ri()
    T[a-1] = max(T[a-1], H[b-1])
    T[b-1] = max(T[b-1], H[a-1])

print(sum(1 for i, h in enumerate(T) if h == 0 or h < H[i]))

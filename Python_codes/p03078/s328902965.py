from heapq import heappush, heappop

X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

q = []
x = y = z = 0
heappush(q, (-(A[x] + B[y] + C[z]), (x, y, z)))
done = set((0, 0, 0))
ans = []
for _ in range(K):
    val, (x, y, z) = heappop(q)
    ans.append(-val)
    for i, j, k in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
        nx = x + i; ny = y + j; nz = z + k
        if nx < X and ny < Y and nz < Z and (nx, ny, nz) not in done:
            heappush(q, (-(A[nx] + B[ny] + C[nz]), (nx, ny, nz)))
            done.add((nx, ny, nz))

print(*ans, sep='\n')

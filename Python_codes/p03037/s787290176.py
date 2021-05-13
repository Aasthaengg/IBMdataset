N, M = map(int, input().split())
c = [0 for i in range(N+1)]
for x in range(M):
    L, R = map(int, input().split())
    c[L-1] += 1
    c[R] -= 1
r = 0
t = 0
for x in c[:-1]:
    t += x
    if t == M:
        r += 1
print(r)

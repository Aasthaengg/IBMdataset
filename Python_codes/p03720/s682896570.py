N, M = map(int, input().split())
dict = {}

for i in range(N):
    dict[str(i+1)] = 0
for i in range(M):
    ai, bi = input().split()
    dict[ai] += 1
    dict[bi] += 1

for i in range(N):
    print(dict[str(i+1)])

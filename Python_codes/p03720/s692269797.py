N, M = map(int, input().split())

ab = [[] for _ in range(M)]
for i in range(len(ab)):
    ab[i] = list(map(int, input().split()))

dict = {}
for i in range(N):
    dict[i + 1] = 0

for i in range(len(ab)):
    dict[ab[i][0]] += 1
    dict[ab[i][1]] += 1

for i in range(N):
    print(dict[i + 1])

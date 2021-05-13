N, M = map(int, input().split())
lefts = []
rights = []

for _ in range(M):
    L, R = map(int, input().split())
    lefts.append(L)
    rights.append(R)

lefts.sort()
rights.sort()

if lefts[-1] > rights[0]:
    print(0)
else:
    print(rights[0] - lefts[-1] + 1)

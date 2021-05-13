N, M = map(int, input().split())

serv1 = set()
servN = set()
for _ in range(M):
    a, b = map(int, input().split())
    if a != 1 and b != N:
        continue

    if a == 1:
        serv1.add(b)
    elif b == N:
        servN.add(a)

print("POSSIBLE" if len(serv1.intersection(servN)) > 0 else "IMPOSSIBLE")

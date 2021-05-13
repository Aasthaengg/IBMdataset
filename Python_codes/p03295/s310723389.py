N, M = [int(s) for s in input().split()]
query = []
for _ in range(M):
    x, y = input().split()
    query.append((int(x), int(y)))

query = sorted(query, key=lambda x: x[1])
b_prev = 0
cnt = 0
for a, b in query:
    if b_prev <= a:
        cnt += 1
        b_prev = b

print(cnt)

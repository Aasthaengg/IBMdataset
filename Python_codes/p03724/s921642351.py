N, M = map(int, input().split())

tree = [0]*(N-1)

for i in range(M):
    a, b = map(int, input().split())
    if a == 1:
        tree[b-2] += 1
    elif b == 1:
        tree[a-2] += 1
    else:
        tree[a-2] += 1
        tree[b-2] += 1

if all(tree[i] % 2 == 0 for i in range(N-1)):
    print('YES')
else:
    print('NO')
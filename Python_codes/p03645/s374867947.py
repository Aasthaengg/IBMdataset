N, M = map(int, input().split())
check = [0] * N
check[0] = 1
ab = []
for i in range(M):
    a, b = map(int, input().split())
    ab.append([a, b])
    if a == 1:
        check[b-1] = 1

for a, b in ab:
    if check[a-1] == 1 and b == N:
        print('POSSIBLE')
        break
else:
    print('IMPOSSIBLE')

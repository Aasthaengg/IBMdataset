N, K, Q = map(int, input().split())
A = []
for _ in range(Q):
    A.append(int(input()) - 1)

border_line = 0
points = [K]*N

for i in range(Q):
    points[A[i]] += 1
    border_line += 1

for j in range(N):
    if points[j] - border_line > 0:
        print('Yes')
    else:
        print('No')
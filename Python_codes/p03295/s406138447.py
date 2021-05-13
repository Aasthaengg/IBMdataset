N, M = map(int, input().split())
B = []
for i in range(M):
    a, b = map(int, input().split())
    B.append([a, b])
B.sort(key=lambda x:x[1])
c = 1
r = B[0][1]
for i in range(1, M):
    if r <= B[i][0]:
        c += 1
        r = B[i][1]
print(c)
H,W = map(int, input().split())
input()
A = list(map(int, input().split()))
s = [[0] * W for _ in range(H)]
index = 0
for i in range(H):
    r = range(W)
    if i % 2 == 1: r = reversed(r)
    for j in r:
        if A[index] == 0:
            index += 1
        s[i][j] = index + 1
        A[index] -= 1

for i in range(H):
    print(' '.join(map(str, s[i])))

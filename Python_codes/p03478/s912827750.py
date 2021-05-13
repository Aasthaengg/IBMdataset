N, A, B = map(int, input().split())
C = 0
for i in range(1, N + 1):
    L = list(str(i))
    c = 0
    for l in L:
        c += int(l)
    if A <= c <= B:
        C += i
print(C)
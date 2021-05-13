n, m, l = map(int, input().split(' '))
i = 0
A = []
while i < n:
    A.append(list(map(int, input().split(' '))))
    i += 1
j = 0
B = []
while j < m:
    B.append(list(map(int, input().split(' '))))
    j += 1
C = []
k = 0
while k < n:
    c0 = []
    p = 0
    while p < l:
        c1 = 0
        q = 0
        while q < m:
            c1 += A[k][q] * B[q][p]
            q += 1
        c0.append(c1)
        p += 1
    C.append(c0)
    k += 1
ans = ''
r = 0
while r < n:
    ans += ' '.join(map(str, C[r])) + '\n'
    r += 1
print(ans[:-1])

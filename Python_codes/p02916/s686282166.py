N,  *_ABC,  = map(int, open(0).read().split())

A = _ABC[:N]
B = _ABC[N: 2*N]
C = _ABC[2*N:]

ans = 0

for i, a in enumerate(A):
    ans += B[a-1]

    if i != len(A)-1 and A[i+1] == a + 1:
        ans += C[a-1]

print(ans)
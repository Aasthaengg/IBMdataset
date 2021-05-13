N = int(input())
A = list(map(int, input().split()))

Q = int(input())

counter = [0 for _ in range(10**5+1)]
ans = 0

for i in range(N):
    counter[A[i]] += 1
    ans += A[i]

B = []
C = []
for i in range(Q):
    Bi, Ci = list(map(int, input().split()))
    B.append(Bi)
    C.append(Ci)

for i in range(Q):
    Bi = B[i]
    Ci = C[i]
    ans += Ci*counter[Bi] - Bi*counter[Bi]
    print(ans)
    counter[Ci] += counter[Bi]
    counter[Bi] = 0

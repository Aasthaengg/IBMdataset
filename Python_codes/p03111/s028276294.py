N, A, B, C = [int(i) for i in input().split()]
L = [int(input()) for _ in range(N)]
ans = float("inf")
for i in range(2 ** (N * 2)):
    a = b = c = 0
    cnt = 0
    for j in range(N):
        bit = i & 3
        if bit == 1:
            a += L[j]
        elif bit == 2:
            b += L[j]
        elif bit == 3:
            c += L[j]
        if bit:
            cnt += 1
        i >>= 2
    if a and b and c:
        ans = min(ans, (cnt - 3) * 10 + abs(A - a) + abs(B - b) + abs(C - c))
print(ans)
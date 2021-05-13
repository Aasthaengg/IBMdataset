n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort()
B.sort()
C.sort()

ans = n ** 3
up = [0] * n
mid = [0] * n
bottom = [0] * n

p = 0
for i in range(n):
    while p < n and A[i] >= B[p]:
        p += 1
    mid[i] = p

p = 0
q = 0
for i in range(n):
    while p < n and B[i] >= C[p]:
        p += 1
    while q < n and B[i] > A[q]:
        q += 1
    bottom[i] = p
    up[i] = q

for m in mid:
    ans -= m * n

for u, b in zip(up, bottom):
    ans -= u * b

print(ans)

N = int(input())
A = list(map(int, input().split()))
A_abs = []
for a in A:
    A_abs.append(abs(a))

ans = []
m = max(A_abs)
midx = A_abs.index(m)

print(2 * N - 2)

for i in range(N):
    if not i == midx:
        print(str(midx + 1) + ' ' + str(i + 1))

for i in range(N - 1):
    if A[midx] >= 0:
        print(str(i + 1) + ' ' + str(i + 2))
    else:
        print(str(N - i) + ' ' + str(N - i - 1))

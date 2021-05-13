N = int(input())
A = list(map(int, input().split()))
R = []

tmp = 0
pm = -1
for i in range(N):
    pm *= -1
    tmp += A[i] * pm
R.append(tmp)

for i in range(1, N):
    tmp = 2 * A[i-1] - R[i-1]
    R.append(tmp)

print(*R)
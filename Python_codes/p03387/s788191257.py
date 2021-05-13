A = list(map(int, input().split()))
A.sort()
ans = 0
tmp = A[2] - A[1]
ans += tmp
A[0] += tmp

if (A[2] - A[0]) % 2 == 0:
    tmp = (A[2] - A[0]) / 2
    ans += tmp
else:
    tmp = (A[2] - A[0] + 1) / 2 + 1
    ans += tmp

print(int(ans))
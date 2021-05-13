N, M = map(int, input().split())
A = list(map(int, input().split()))

s = sum(A)
th = s / (4*M)
cnt = 0

for a in A:
    if a >= th:
        cnt += 1

if cnt < M:
    print("No")
else:
    print("Yes")
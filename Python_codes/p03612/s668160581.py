n = int(input())
A = list(map(int, input().split()))
cnt = 0
for i in range(n):
    now = A[i]
    if now == i + 1:
        cnt += 1
        if i + 1 < n:
            nex = A[i + 1]
            if nex == i + 2:
                A[i + 1] = now
                continue
print(cnt)

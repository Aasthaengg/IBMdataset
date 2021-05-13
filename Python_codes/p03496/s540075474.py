N = int(input())
A = list(map(int,input().split()))

M = max(A)
Mi = A.index(M)
m = min(A)
mi = A.index(m)

cnt = 0
ans = []

if M > 0 and m < 0:
    if abs(m) <= abs(M):
        for i in range(N):
            if Mi == i:
                continue
            x = Mi
            y = i
            A[y] += A[x]
            ans.append((x, y))
            cnt += 1
    else:
        for i in range(N):
            if mi == i:
                continue
            x = mi
            y = i
            A[y] += A[x]
            ans.append((x, y))
            cnt += 1

M = max(A)
m = min(A)

if m >= 0:
    for i in range(N-1):
        x = i
        y = i+1
        A[y] += A[x]
        ans.append((x, y))
        cnt += 1
else:
    for i in range(N-1, 0, -1):
        x = i
        y = i-1
        A[y] += A[x]
        ans.append((x, y))
        cnt += 1

print(cnt)
for x, y in ans:
    print(x+1, y+1)
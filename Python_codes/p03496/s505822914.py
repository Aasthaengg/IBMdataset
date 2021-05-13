n = int(input())
A = list(map(int, input().split()))

M = max(A)
m = min(A)
for i, a in enumerate(A):
    if a == M:
        max_id = i
    if a == m:
        min_id = i

ans = []
if m >= 0:
    for i in range(n-1):
        ans.append((i+1, i+2))
elif M <= 0:
    for i in reversed(range(1, n)):
        ans.append((i+1, i))
else:
    if abs(M) >= abs(m):
        for i, a in enumerate(A):
            if a < 0:
                ans.append((max_id+1, i+1))
        for i in range(n-1):
            ans.append((i+1, i+2))
    else:
        for i, a in enumerate(A):
            if a > 0:
                ans.append((min_id+1, i+1))
        for i in reversed(range(1, n)):
            ans.append((i+1, i))
print(len(ans))
for i in range(len(ans)):
    print(*ans[i])

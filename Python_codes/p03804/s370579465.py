n, m = map(int, input().split())
A = [input() for i in range(n)]
B = [input() for i in range(m)]

ans = 'No'
for i in range(n - m + 1):
    for j in range(n - m + 1):
        C = []
        for k in range(m):
            C.append(A[i + k][j : j + m])
        if B == C:
            ans = 'Yes'
            
print(ans)
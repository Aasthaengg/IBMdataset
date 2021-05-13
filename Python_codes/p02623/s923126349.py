n, m, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_cumsum, B_cumsum = [0], [0]

for i in range(n):
    A_cumsum.append(A_cumsum[i] + A[i])
    
for j in range(m):
    B_cumsum.append(B_cumsum[j] + B[j])
    
ans, j = 0, m

for i in range(n + 1): # 0を最初に代入した分
    if A_cumsum[i] > k:
        break
    while A_cumsum[i] + B_cumsum[j] > k:
        j -= 1
    ans = max(ans, i + j)

print(ans)
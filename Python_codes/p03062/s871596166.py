N = int(input())
A = list(map(int, input().split()))

if 0 in A:
    ans = 0
    for i in range(N):
        ans += max(A[i], -A[i])
    print(ans)
    exit()
    
minus_count = 0
for i in range(N):
    if A[i] < 0:
        minus_count += 1
        
if minus_count % 2 == 0:
    ans = 0
    for i in range(N):
        ans += max(A[i], -A[i])
    print(ans)
else:
    for i in range(N):
        if A[i] < 0:
            A[i] = -A[i]
    min_A = min(A)
    print(sum(A) - 2*min_A)
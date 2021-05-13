n, m, c = map(int, input().split())
 
B = list(map(int, input().split()))
ans = 0
 
for i in range(n):
    A = list(map(int, input().split()))
    x = 0
 
    for j in range(m):
        x += A[j]* B[j]
    x += c
    if x > 0:
        ans += 1

print(ans)
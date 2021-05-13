n,m,c = map(int,input().split())
B = list(map(int,input().split()))

ans = 0
for _ in range(n):
    temp = c
    A = list(map(int,input().split()))
    for i in range(m):
        temp += B[i]*A[i]
    
    if temp > 0:
        ans += 1

print(ans)

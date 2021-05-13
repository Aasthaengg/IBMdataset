N,M,D = map(int,input().split())

B = list(map(int,input().split()))

ans = 0

for _ in range(N):
    tmp_math = D
    A = list(map(int,input().split()))
    for i in range(M):
        tmp_math += B[i]*A[i]
    if tmp_math > 0:
        ans += 1
print(ans)
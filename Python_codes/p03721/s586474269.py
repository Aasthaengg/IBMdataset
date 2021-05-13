N,K = map(int,input().split())
A = sorted([list(map(int,input().split())) for _ in range(N)],key=lambda x:x[0])
cnt = 0
i = 0
while i<N:
    a,b = A[i]
    if cnt+b<=K:
        cnt += b
    else:
        break
    i += 1
if cnt==K:
    print(A[i-1][0])
else:
    print(A[i][0])
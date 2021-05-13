N,M = map(int,input().split())
A = sorted(list(map(int,input().split())))
B = sorted([list(map(int,input().split())) for _ in range(M)],key=lambda x:x[1],reverse=True)
cur = 0
cnt = B[0][0]
for i in range(N):
    a = A[i]
    if cur<M and B[cur][1]>a:
        if cnt>0:
            A[i] = B[cur][1]
            cnt -= 1
        else:
            cur += 1
            if cur<M:
                cnt = B[cur][0]
                if B[cur][1]>a:
                    A[i] = B[cur][1]
                    cnt -= 1
print(sum(A))
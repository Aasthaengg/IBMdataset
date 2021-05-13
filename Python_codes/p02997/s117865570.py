N, K = map(int, input().split())
P = (N-1)*(N-2)//2
if K > P:
    print(-1)
    exit()
M = (N-1)+ (P-K)
print(M)
for i in range(2,N+1):
    print(1, i)
cnt = 1
i = 2
j = i+1
while cnt <= P-K:
    if j > N:
        i+= 1
        j = i+1
    print(i, j)
    j += 1
    cnt += 1

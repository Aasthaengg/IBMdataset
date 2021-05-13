N, K = map(int, input().split())

cnt = 0
for b in range(K+1,N+1):
    x = (b-K)*(N//b) + max(0,(N%b)-K+1)
    # print(b,"num",x)
    cnt+= x

if K == 0:
    print(N**2)
else:
    print(cnt)
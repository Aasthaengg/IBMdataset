N,M=map(int,input().split())
if N >= M//2:
    print(M//2)
    exit()
ans = N
rest_c = M - N*2
ans += rest_c // 4
print(ans)
N,M = map(int, input().split())
if 2*N > M:
    cnt = M//2
else:
    cnt = N
    M -= 2*cnt
    cnt += M//4
print(cnt)
N = int(input())
A = list(map(int, input().split()))
cnt = 0
for i in range(3**N):
    ii = i
    res = 1
    for j in range(N):
        k = ii % 3
        ii = ii // 3
        res *= (A[j]-1+k)
    if res % 2 == 0:
        cnt += 1
print(cnt)
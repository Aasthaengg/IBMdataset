N, K = map(int, input().split())

cnt = 0
for j in range(K+1, N+1):
    block = N // j
    R = N % j
    cnt += block * (j-1-K+1)
    if R:
        cnt += max(0, R - max(K,1) +1)
    #print(j, block, block * (j-1-K+1), max(0, R - K +1))
print(cnt)
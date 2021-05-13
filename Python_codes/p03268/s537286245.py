N, K = [int(i) for i in input().split()]
cnt = 0
if K % 2 == 0:
    for i in range(1, 2*N//K+1):
        cnt += 1 + (2*N//K-i)//2 * 6 + (2*N//K-i)//2 * ((2*N//K-i)//2 - 1) * 3
else:
    for i in range(1, N//K+1):
        cnt += 1 + (N//K-i) * 6 + (N//K-i) * ((N//K-i) - 1) * 3

print(cnt)
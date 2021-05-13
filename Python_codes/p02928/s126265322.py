MOD = 10**9 + 7
N, K = map(int, input().split())
arr = list(map(int, input().split()))
tmp = 0
for i in range(N):
    for k in range(i,N):
        if i == k:
            continue
        if arr[i] > arr[k]:
            tmp += 1
tmp2 = 0
for i in range(N):
    for k in range(N):
        if i == k:
            continue
        if arr[i] > arr[k]:
            tmp2 += 1
print((tmp*K+(((K-1)*K)//2)*tmp2)%MOD)
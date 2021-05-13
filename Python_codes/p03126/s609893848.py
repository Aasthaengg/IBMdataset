N, M = map(int, input().split())

ans = [0 for i in range(M)]
for i in range(N):
    KM = list(map(int, input().split()))
    for j in range(1, len(KM)):
        ans[KM[j]-1] += 1

count = 0
for i in range(M):
    if ans[i] == N:
        count += 1
        
print(count)
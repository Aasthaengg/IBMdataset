N,K = map(int,input().split())
A = list(map(int,input().split()))

li = [0 for i in range(40)]

for i in range(N):
    j = 0
    while((A[i]>>j) > 0):
        if (A[i]>>j)&1:
            li[j] += 1
        j += 1

mm = 0
for j in range(39,-1,-1):
    if li[j] <= N-li[j]:
        if (mm + (1<<j)) <= K:
            mm += 1<<j

ans = 0
for n in range(N):
    ans += mm^A[n]

print(ans)


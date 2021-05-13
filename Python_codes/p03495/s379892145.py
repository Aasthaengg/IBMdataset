n, k = map(int, input().split())
lis = list(map(int, input().split()))

count = [0]*(n+1)

for i in range(n):
    count[lis[i]] += 1

cnt = sorted(count)
nlis = []
for i in range(n+1):
    if cnt[i] != 0:
        nlis.append(cnt[i])
if len(nlis) <= k:
    print(0)
    exit()

ans = 0
for i in range(len(nlis)-k):
    ans += nlis[i]
    
print(ans)
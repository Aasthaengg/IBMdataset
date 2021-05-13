N,M=map(int,input().split())
like = [0]*M

for _ in range(N):
    items = list(map(int,input().split()))
    for i in range(1,len(items)):
        like[items[i]-1] += 1

ans = 0
for i in range(M):
    if like[i] == N:
        ans += 1

print(ans)
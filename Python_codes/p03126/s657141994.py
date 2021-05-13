N, M = map(int,input().split())
like = [0 for i in range(M+1)]

for i in range(N):
    KA = list(map(int,input().split()))

    for k in range(1,KA[0]+1):
        like[KA[k]] += 1
        
ans = 0
for i in range(M+1):
    if like[i] == N:
        ans += 1

print(ans)
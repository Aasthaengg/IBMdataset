N,M = map(int,input().split())
lis = [0] * N
for i in range(M):
    a,b = map(int,input().split())
    lis[a-1] += 1
    lis[b-1] += 1
ans = 'YES'
for i in lis:
    if i % 2 == 1:
        ans = 'NO'
print(ans)

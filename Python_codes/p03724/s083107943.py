N,M = map(int,input().split())
ver = [0] * N
for i in range(M):
    a,b = map(int,input().split())
    ver[a-1] += 1
    ver[b-1] += 1
ans = 'YES'
for i in range(N):
    if ver[i] % 2 != 0:
        ans = 'NO'
print(ans)


N = int(input())
A = list(map(int,input().split()))
M = 1000001
cnt = [0]*M
ans = 0
for x in A:
    if cnt[x] != 0:
        cnt[x] = 2
        continue
    for i in range(x,M,x):
        cnt[i] += 1
for x in A:
    if cnt[x] == 1:
        ans += 1
print(ans)

    

n = int(input())
h = list(map(int,input().split()))
cnt = 0
tmp = h[0]
ans = 0
for i in range(1,n):
    if tmp >= h[i]:
        cnt += 1
    else:
        ans = max(ans,cnt)
        cnt = 0
    tmp = h[i]
ans = max(ans,cnt)
print(ans)
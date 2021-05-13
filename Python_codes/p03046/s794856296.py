m,k = map(int,input().split())
if k>=2**m:
    print(-1)
    exit()
if m == 1:
    if k == 0:
        print(0,0,1,1)
    else:
        print(-1)
    exit()
ans = [0 for _ in range(2**(m+1))]
for i in range(2**m):
    if i < k:
        ans[i] = i
        ans[2**(m+1)-2-i] = i
    if i == k:
        continue
    if i > k:
        ans[i-1] = i
        ans[2**(m+1)-i-1] = i
ans[2**m-1] = k
ans[2**(m+1)-1] = k
print(*ans,sep=" ")
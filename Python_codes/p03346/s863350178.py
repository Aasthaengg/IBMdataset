n = int(input())
lis = [int(input()) for i in range(n)]
li = [-1 for i in range(n)]
for i in range(n):
    li[lis[i]-1] = i
cnt = 0
ans = n-1
for i in range(n-1):
    if li[i] < li[i+1]:
        cnt += 1
    else:
        ans = min(ans,n-1-cnt)
        cnt = 0
ans = min(ans,n-1-cnt)
print(ans)
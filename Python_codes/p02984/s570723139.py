n = int(input())
a = list(map(int,input().split()))
ans = [0]
for i in range(n-1):
    ans.append(a[i]-ans[i])
ans[0] = a[-1]-(ans[0]+ans[-1])
for i in range(1,n):
    ans[i] = (a[i-1]-ans[i-1]//2)*2
print(*ans)

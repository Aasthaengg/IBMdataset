n,t = map(int,input().split())
a = list(map(int,input().split()))
ans = [0]*n
flag = float("inf")
for i in range(n):
    flag = min(flag,a[i])
    ans[i] = a[i]-flag
print(ans.count(max(ans)))
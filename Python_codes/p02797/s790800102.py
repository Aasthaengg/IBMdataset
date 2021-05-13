n,k,s = map(int,input().split())
ans = [10**9]*n
if s != 10**9:
    for i in range(k):
        ans[i] = s
else:
    ans = [1] * n
    for i in range(k):
        ans[i] = s
print(" ".join(map(str, ans)))

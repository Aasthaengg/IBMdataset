n,m = map(int,input().split())
ans = ['Yes'] * m
for i in range(n):
    k = list(map(int,input().split()))
    k.pop(0)
    for i in range(m):
        if not i + 1 in k:
            ans[i] = 'No'
print(ans.count('Yes'))
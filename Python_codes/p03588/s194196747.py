#%%
n = int(input())
a = [[] for _ in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))
a.sort()
x, y = a[-1][0], a[-1][1]
ans = x + y
print(ans)


#%%

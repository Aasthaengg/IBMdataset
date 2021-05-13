#%%
n = int(input())
a = list(map(int,input().split()))

s = sum(a) / len(a)

ans = 0
tmp = 10**9

for i in range(n):
    if tmp > abs(s-a[i]):
        ans = i
        tmp = abs(s-a[i])

print(ans)


#%%

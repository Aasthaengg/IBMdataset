#%%
n, k = map(int, input().split())
if n - 1 >= 2*(k-1):
    print('YES')
else:
    print('NO')
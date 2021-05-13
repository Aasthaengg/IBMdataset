#%%
n, a, b = map(int, input().split())
ans1 = min(a, b)
ans2 = max(a + b - n, 0)
ans = ' '.join([str(ans1), str(ans2)]) 
print(ans)
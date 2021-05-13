n = int(input())
a = [int(input()) for i in range(n)]
not10 = [i for i in a if i % 10 != 0]
a10 = [i for i in a if i % 10 == 0]
maxn10 = sum(not10)
if maxn10 % 10 == 0 and maxn10:
    maxn10 -= min(not10)
ans = maxn10 + sum(a10)
print(0) if ans % 10 == 0 else print(ans)

from itertools import product

n = int(input())
data = {}
for p in range(1, n+1):
    a = int(input())
    # 人p=1～の証言
    data[p] = [list(map(int, input().split())) for _ in range(a)]
    
# パターン生成
ans = 0
for honest in product(range(2), repeat=n):
    for p,hk in enumerate(honest, 1):
        if hk == 1:
            # 証言の矛盾をチェック
            if not all([honest[x-1] == y for x,y in data[p]]):
                break
    else:
        ans = max(ans, sum(honest))

print(ans)
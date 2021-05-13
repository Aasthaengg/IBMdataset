# 夏休みN日間
# 宿題はM個出されており、i番目の宿題をやるにはj日間かかる。
# この場合、宿題を全部終わらせるのに ...日かかる

n, m = map(int, input().split())
days = list(map(int, input().split()))

# 宿題が全てが終わる場合
if n - sum(days) >= 0:
    print(n - sum(days))
# 宿題終わらない場合
else:
    print(-1)
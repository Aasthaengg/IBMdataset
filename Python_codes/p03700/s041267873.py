from math import ceil

N,A,B = map(int,input().split())
h = sorted([int(input()) for _ in range(N)], reverse=True)

# C回以下の爆発で倒せるか
def is_all_kill(C:int):
    cnt = 0
    for HP in h:
        # あるモンスターに中心ダメージを何回与えるか
        tmp = ceil((HP-B*C)/(A-B))
        # オーバーキルの場合
        if tmp <= 0:
            break
        cnt += tmp
    return cnt <= C

ok = 10 ** 18
ng = 0
while ok - ng > 1:
    mid = (ok + ng) // 2
    if is_all_kill(mid):
        ok = mid
    else:
        ng = mid

print(ok)
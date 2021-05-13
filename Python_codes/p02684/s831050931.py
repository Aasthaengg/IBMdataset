# 一度同じ場所についたら、そこからのループ回数をもう一度求める方法でやってみる
import sys
n,k = map(int,input().split())
a_ls = list(map(int, input().split()))
for i in range(n):
    a_ls[i] -= 1
town_done = [0] * n

# 初期状態のセット
now_town = 0
times = 0
while True:
    # きたtownに関する処理
    town_done[now_town] = 1
    
    # 次の移動
    now_town = a_ls[now_town]
    times += 1
    if times == k:
        print(now_town+1)
        sys.exit()
    if town_done[now_town]:
        base = now_town
        break

rest = k - times
times = 0
while True:
    now_town = a_ls[now_town]
    times += 1
    rest -= 1
    if now_town == base:
        times_per_loop = times
        break
    if rest == 0:
        print(now_town+1)
        sys.exit()

rest = rest % times_per_loop
for _ in range(rest):
    now_town = a_ls[now_town]
print(now_town+1)
import heapq

def check(h, T, A, B):
    # T回の爆破でいける？ -> BがT回行われる下で、残ったモンスターをT回のA - Bダメ攻撃で倒せる？
    que = []
    for hi in h:
        if hi - B * T > 0:
            que.append(- hi + B * T)
    que.sort()
    A_count = 0
    for q in que:
        count = (-q + (A - B) - 1) // (A - B)
        A_count += count
    
    return A_count <= T


N, A, B = map(int, input().split(" "))
h = []
for _ in range(N):
    h.append(int(input()))

lower, upper = 0, 10 ** 15

while upper - lower > 1:
    mid = (upper + lower) // 2
    if check(h, mid, A, B):
        upper = mid
    else:
        lower = mid

print(upper)
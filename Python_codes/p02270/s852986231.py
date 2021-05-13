n, k = map(int, input().split())
W = [int(input()) for _ in range(n)]

left = 0
right = 10000 * n

def Chech(P,k,arr):
    weight = 0
    n_trucks = 1
    for i,a in enumerate(arr):
        # iの荷物について積むかどうか決め、それに応じてトラックの数を増加させる
        if P < a:
            return i
        if weight +a <= P:
            weight += a
        else:
            n_trucks += 1  # Pを超えるなら次のtruckを用意
            weight = a  # 新たなトラックに積んでいる
        if n_trucks == k + 1:  # k+1台目のtruckは存在しない。これまでに積んだ荷物の数を返す
            return i

    return len(arr)  # すべて運べるならlen(arr)を返すとする

# right - left > 0　だと無限ループに入るっぽい
while right - left > 1:
    mid = (left+right)//2
    v = Chech(mid,k,W)

    if v >= n:
        right = mid
    else:
        left = mid

print(right)

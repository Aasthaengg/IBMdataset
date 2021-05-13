N = int(input())
A = list(map(int, input().split()))

right = 0  # 毎回rightを使い回すようにする
res = 0  # 部分列の長さ
xor = 0  # xorも使い回す
s = 0  # sも使い回す

for left in range(N):
    while right < N and (s + A[right] == xor ^ A[right]):  # rightを１個すすめた時に条件を満たす
        s += A[right]
        xor ^= A[right]
        right += 1

    # breakした状態で right は条件を満たす最大
    res += right - left

    # left をインクリメントする準備
    if right == left:  # right が left に重なったら right も動かす
        right += 1
    else:
        # left のみがインクリメントされるので s, xor から A[left] をのぞく
        s -= A[left]
        xor ^= A[left]

print(res)

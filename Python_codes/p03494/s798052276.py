N = int(input())
A = list(map(int, input().split()))

# 操作回数
counter = 0

# 操作が行えなくなるまで操作を行う
while True:
    # // 操作が行えるかどうかを判定する
    can_do = True
    for i in range(N):
        if A[i] % 2 == 1:
            can_do = False

    # 操作を行えないならば、ループを打ち切る
    if not can_do:
        break

    # 操作を行えるならば、操作を行う
    for i in range(N):
        A[i] //= 2

    # 操作回数をカウントする
    counter += 1

print(counter)
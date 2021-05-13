import sys

N, A, B = map(int, sys.stdin.readline().strip().split())

H = []
for _ in range(N):
    H.append(int(sys.stdin.readline().strip()))
H.sort()

# 二分探索でmid回の攻撃で魔物を消し去れるか
left = 1
right = 10**9

# うまくいかないのでansを保持しておく
ans = right
while left < right:
    mid = (left + right) // 2
    # print(mid)
    n = mid
    for h_i in H:
        if h_i <= B * mid:
            continue

        # Bの攻撃のみで消し去れない場合はAの攻撃を消費する
        h_i -= B * mid
        n -= (h_i - 1) // (A-B) + 1

    if n >= 0:
        ans = min(ans, mid)
    if n == 0:
        break
    elif n > 0:
        right = mid
    else:
        left = mid + 1

print(ans)
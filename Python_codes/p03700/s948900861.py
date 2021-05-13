import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

N, A, B = map(int, readline().split())
H = [int(readline()) for _ in range(N)]


def C(T):
    """
    T回爆発させて、魔物全滅できるか
    """
    damage = B * T
    cnt = 0
    for h in H:
        h -= damage
        if h <= 0:
            continue
        cnt += (h + (A - B) - 1) // (A - B)
        if cnt > T:
            return False
    return cnt <= T


left = 0
right = 10 ** 18
while right - left > 1:
    mid = (right + left) // 2
    if C(mid):
        right = mid
    else:
        left = mid

ans = right
print(ans)

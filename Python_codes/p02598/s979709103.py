N, K = map(int, input().split())
A = list(map(int, input().split()))


def f(n):
    cnt = 0
    for a in A:
            # a/nが偶数の場合
        if a % n == 0:
            cnt += a//n-1
        # a/nが奇数の場合
        else:
            cnt += a//n
    return True if K >= cnt else False


l = 0
r = max(A)
# 二分探索
while r - l > 1:
    m = (r+l)//2
    if f(m):
        r = m
    else:
        l = m
print(r)

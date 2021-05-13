n,k = map(int, input().split())
t = [int(input()) for i in range(n)]

def check(p):
    """
    :param p: 最大積載量
    :return: 積むことができる荷物の数
    """
    global k # トラックの台数
    global t # 荷物の重さのリスト
    i = 0
    for _ in range(k):
        remaining = p
        while remaining >= t[i]:
            remaining -= t[i]
            i += 1
            if  i == len(t):
                return i
    return i

lo = 0
hi = 10**6 * 10**4

p = 0

while hi - lo > 1:
    mid = (lo + hi) // 2
    if check(mid) < n:
        lo = mid
    else:
        hi = mid
ans = hi
print(ans)

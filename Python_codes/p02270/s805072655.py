def check(p):
    j = 0 # 積んだ荷物の個数
    for i in range(k):
        track = 0
        while track + w[j] <= p:
            track += w[j]
            j += 1
            if j == n:
                return n
    return j

def solve():
    right = 100000 * 10000
    left = 0
    mid = (right + left) // 2
    while right - left > 0:
        cnt = check(mid)
        if cnt == n:
            right = mid
            mid = (right + left) // 2
        else:
            left = mid + 1
            mid = (right + left) // 2

    return mid

n, k = map(int, input().split())
w = []
for _ in range(n):
    w.append(int(input()))

print(solve())


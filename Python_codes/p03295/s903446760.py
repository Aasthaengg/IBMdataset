import sys
input = sys.stdin.readline
INF = 10**18

def li():
    return [int(x) for x in input().split()]


N, M = li()
# 区間は半開区間 [a, b)
Intervals = [li() for _ in range(M)]

Intervals.sort(key=lambda l: l[1])

last_end = - INF
required_cnt = 0
for interval in Intervals:
    start, end = interval[0], interval[1]
    # 重なってなければ一点必要
    # 半開区間なのでlast_endとstartが等しくても重なってない
    if last_end <= start:
        last_end = end
        required_cnt += 1

print(required_cnt)
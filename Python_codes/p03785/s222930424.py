# https://atcoder.jp/contests/agc011/tasks/agc011_a

n, c, k = map(int, input().split())

schedule = []
for _ in range(n):
    t = int(input())
    schedule.append(t)
schedule.sort()
# schedule.append(float('inf'))

def check(num, schedule, c, k):
    bus = 0
    start = schedule[0]
    p = 0
    i = 0
    while i < len(schedule):
        s = schedule[i]
        if s <= start + k:
            p += 1
            i += 1
            if p == c:
                bus += 1
                p = 0
                if i == len(schedule):
                    break
                start = schedule[i]
        else:
            start = schedule[i]
            bus += 1
            p = 1
            i += 1
    if p:
        bus += 1
    if bus <= num:
        return True
    return False

l = 0
r = 10 ** 10
ans = float('inf')
while l <= r:
    mid = (l + r) // 2
    if check(mid, schedule, c, k):
        r = mid - 1
        ans = min(ans, mid)
    else:
        l = mid + 1

print(ans)

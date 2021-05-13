# https://atcoder.jp/contests/agc011/tasks/agc011_a

n, c, k = map(int, input().split())

schedule = []
for _ in range(n):
    t = int(input())
    schedule.append(t)
schedule.sort()

ans = 0
start = schedule[0]
p = 0
for i in range(n):
    s = schedule[i]
    if s <= start + k:
        p += 1
        if p == c:
            ans += 1
            p = 0
            if i + 1 == n:
                break
            start = schedule[i + 1]
    else:
        ans += 1
        start = schedule[i]
        p = 1
if p:
    ans += 1
print(ans)

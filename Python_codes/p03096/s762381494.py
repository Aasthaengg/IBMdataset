n = int(input())
c = [int(input()) for _ in range(n)]
mod = 10 ** 9 + 7
MAX = 2 * 10 ** 5

cc = []
prev = 0
for e in c:
    if e != prev:
        cc.append(e)
        prev = e

ln = len(cc)

dp_prev = 1
acc = [0] * (MAX + 1)

for i, e in enumerate(cc, 1):
    dp_now = dp_prev + acc[e]
    dp_now %= mod

    acc[e] += dp_prev
    acc[e] %= mod

    dp_prev = dp_now

print(dp_now)

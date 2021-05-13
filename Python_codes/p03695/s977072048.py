#!/usr/local/bin/python3
# https://atcoder.jp/contests/abc064/tasks/abc064_c


def check(a):
    if a < 400:
        return 0
    elif a < 800:
        return 1
    elif a < 1200:
        return 2
    elif a < 1600:
        return 3
    elif a < 2000:
        return 4
    elif a < 2400:
        return 5
    elif a < 2800:
        return 6
    elif a < 3200:
        return 7
    else:
        return 8


N = int(input())
A = list(map(int, input().split()))

ratings = [
    '1-399', '400-799', '800-1199', '1200-1599', '1600-1999',
    '2000-2399', '2400-2799', '2800-3199', '3200-']
d = {r: 0 for r in ratings}

for a in A:
    d[ratings[check(a)]] += 1

ans = 0
for k, v in d.items():
    if k != '3200-' and v != 0:
        ans += 1

top = d['3200-']
if top == 0:
    print(ans, ans)
elif ans == 0:
    print(1, top)
else:
    print(ans, ans+top)

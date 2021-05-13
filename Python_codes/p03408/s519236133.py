import collections

n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]
money = []
for plus in collections.Counter(s).most_common():
    if plus[0] in t:
        money.append(plus[1] - collections.Counter(t).get(plus[0]))
    else:
        money.append(plus[1])
if max(money) < 0:
    print(0)
else:
    print(max(money))
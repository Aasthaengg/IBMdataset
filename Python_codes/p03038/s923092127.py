from collections import Counter
n_cards, n_change = map(int,input().split())
a_ls = list(map(int, input().split()))
c = Counter(a_ls)
for i in range(n_change):
    time, card = map(int,input().split())
    c[card] += time

d = sorted(c.items(),key=lambda x:x[0], reverse=True)
ans = 0
rest = n_cards
for v, times in d:
    if times <= rest:
        ans += v*times
        rest -= times
    else:
        ans += v*rest
        break
print(ans)
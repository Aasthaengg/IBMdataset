from collections import Counter

count = Counter([])

N = int(input())

for i in range(2,N+1):
    n = i
    tmp = []
    d = 2
    while d <= n:
        while n%d == 0:
            n //= d
            tmp.append(d)
        d += 1
    count += Counter(tmp)

ans = 0
#74個以上の次数をもつ素因数を探す
for v in count.values():
    if v >= 74:
        ans += 1

#24,2個以上の次数の組み合わせ
more24 = 0
more2 = 0
for v in count.values():
    if v >= 2:
        more2 += 1
    if v >= 24:
        more24 += 1

ans += more24*(more2-more24)
ans += more24*(more24-1)

#14,4個以上の次数の組み合わせ
more14 = 0
more4 = 0
for v in count.values():
    if v >= 4:
        more4 += 1
    if v >= 14:
        more14 += 1
ans += more14 * (more4-more14)
ans += more14*(more14-1)

#4,4,2個以上の次数の組み合わせ
ans += more4*(more4-1)//2 * (more2-more4)
ans += more4*(more4-1)//2*(more4-2)

print(ans)
d = int(input())
c = list(map(int, input().split(' ')))

s = [list(map(int, input().split(' '))) for _ in range(d)]

t = [int(input()) - 1 for _ in range(d)]
ca = [0] * 26 # 放置された不満の数々
dc = 0 # カレントな満足度
dl = [] # 満足度のログ

for i in range(1, d + 1):
    dc += s[i - 1][t[i - 1]]
    ca[t[i - 1]] = i
    dc -= sum([c[i2] * (i - ca[i2]) for i2 in range(26)])
    dl.append(dc)
print('\n'.join(list(map(str, dl))))
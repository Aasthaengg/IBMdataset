# completeするsetを決め打って考える。

from itertools import product

d, g = map(int, input().split())
ans = 10 ** 10
PC = [list(map(int, input().split())) for _ in range(d)]
kumiawase = list(product([1, 0], repeat=d))
for kumi in kumiawase:
    cnt = 0
    temp = 0
    unused = []
    for i in range(d):
        p, c = PC[i]
        if kumi[i] == 1:
            temp += (i + 1) * 100 * p
            temp += c
            cnt += p
        else:
            unused.append(((i + 1) * 100, p))
    if temp >= g:
        ans = min(ans, cnt)
    else:
        if not unused:
            continue
        remain = g - temp
        unused.sort(reverse=True)
        saidai, kaisu = unused[0]
        if remain <= (kaisu - 1) * saidai:
            cnt += (remain + saidai - 1) // (saidai)
            ans = min(ans, cnt)

print(ans)

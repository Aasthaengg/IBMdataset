from itertools import accumulate
n,m = map(int, input().split())
a = list(map(int, input().split()))
acc = [0] + list(accumulate(a))
mod = {}
for i in acc:
    d = i%m
    if d not in mod:
        mod[d] = 0
    mod[d] += 1
cnt = 0
for v in mod.values():
    if v:
        cnt += v * (v-1) // 2
print(cnt)

from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
q = int(input())

sm = 0
cnt = defaultdict(int)
for i in a:
    sm += i
    cnt[i] += 1

for _ in range(q):
    b, c = list(map(int, input().split()))
    if b in cnt:
        sm -= cnt[b] * b
        sm += cnt[b] * c

        cnt[c] += cnt[b]
        del cnt[b]
    print(sm)
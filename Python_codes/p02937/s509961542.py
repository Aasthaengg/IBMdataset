from bisect import bisect_left

s = input()
t = input()

l = len(s)

ss = s * 2
let = [[] for _ in range(26)]
for i, e in enumerate(ss, 1):
    idx = ord(e) - ord("a")
    let[idx].append(i)

for e in t:
    idx = ord(e) - ord("a")
    if not let[idx]:
        print(-1)
        exit()

i = 1
times = 0
for e in t:
    j = ord(e) - ord("a")
    choose = bisect_left(let[j], i)
    q, r = divmod(let[j][choose], l)
    times += q
    i = r + 1

ans = times * l + i - 1
print(ans)

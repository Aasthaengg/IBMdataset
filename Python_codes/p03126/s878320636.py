n, m = map(int, input().split())
k = []
a = []
for _ in range(n):
    words = input().split()
    k.append(int(words[0]))
    a.append(list(map(int, words[1:])))

like_cnt = {i: 0 for i in range(1, m + 1)}
for ai in a:
    for aij in ai:
        like_cnt[aij] += 1
print(list(like_cnt.values()).count(n))

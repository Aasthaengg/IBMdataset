s = input()
len_s = len(s)
cnt = 0
enemy = []
me = []
INF = 1e10
for i, _s in enumerate(s):
    if _s == "p":
        cnt += 1
    enemy.append(cnt)
    me.append((i+1) // 2)
    diff = (i + 1) // 2 - cnt
print(diff)
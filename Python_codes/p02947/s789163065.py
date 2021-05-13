n = int(input())
d = {}
for _ in range(n):
    s = list(input())
    s.sort()
    js = ''.join(s)
    if js in d:
        d[js] += 1
    else:
        d[js] = 1

cnt = 0
for v in d.values():
    cnt += (v*(v-1)//2)
print(cnt)
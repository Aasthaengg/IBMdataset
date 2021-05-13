N, *d = map(int, open(0).read().split())

d.sort(reverse = True)
cnt = 0

pre = d[0]

for i in d:
    if cnt != 0 and pre == i:
        continue
    cnt += 1
    pre = i

print(cnt)
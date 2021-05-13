import sys
n, m = map(int, input().split())

cnt = {}
for i in range(m):
    s, c = map(int, input().split())
    if cnt.get(s) is not None and cnt[s] != c:
        print(-1)
        sys.exit()
    cnt[s] = c

for i in range(10**n):
    si = str(i)
    if len(si) != n: continue

    flg = 0
    for j in range(n):
        if cnt.get(j + 1) is None:
            continue
        if si[j] == str(cnt[j + 1]):
            flg += 1
    if flg == len(cnt):
        print(i)
        sys.exit()
print(-1)

import sys
input = sys.stdin.readline

n,h = map(int,input().split())
l = []
wield_max = 0
for i in range(n):
    a,b = map(int,input().split())
    l.append((a,b))
    wield_max = max(wield_max,a)

strong_throws = []
for i in range(n):
    if l[i][1] >= wield_max:
        strong_throws.append(l[i][1])

cnt = 0
for throws in sorted(strong_throws,reverse=True):
    h -= throws
    cnt += 1
    if h <= 0:
        print(cnt)
        exit()
cnt += h//wield_max
if h % wield_max != 0:
    cnt += 1
print(cnt)

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
a = list(map(int, readline().split()))
if a[0] > 0:
    cnt2 = a[0] + 1
    now2 = -1
    cnt1 = 0
    now1 = a[0]
elif a[0] == 0:
    cnt2 = 1
    now2 = -1
    cnt1 = 1
    now1 = 1
else:
    cnt2 = 0
    now2 = a[0]
    cnt1 = -a[0] + 1
    now1 = 1
for i, aa in enumerate(a[1:]):
    if i % 2 == 0:
        if aa + now2 > 0:
            now2 += aa
        else:
            cnt2 += abs(now2 + aa) + 1
            now2 = 1
        if now1 + aa < 0:
            now1 += aa
        else:
            cnt1 += now1 + aa + 1
            now1 = -1
    else:
        if aa + now1 > 0:
            now1 += aa
        else:
            cnt1 += abs(now1 + aa) + 1
            now1 = 1
        if now2 + aa < 0:
            now2 += aa
        else:
            cnt2 += now2 + aa + 1
            now2 = -1
print(min(cnt1, cnt2))

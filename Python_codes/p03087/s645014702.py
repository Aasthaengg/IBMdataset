import bisect
n, q = map(int, input().split())
s = input()
cnt = 0
apoint = []
cpoint = []
for i in range(len(s) - 1):
    if s[i] + s[i + 1] == 'AC':
        cnt += 1
        apoint.append(i)
        cpoint.append(i)
# print('cnt:', cnt)
# print('acpoint:', apoint)
for i in range(q):
    l, r = map(int, input().split())
    l, r = l - 1, r - 1
    left = bisect.bisect_left(apoint, l)
    right = bisect.bisect_left(cpoint, r)
    print(right - left)

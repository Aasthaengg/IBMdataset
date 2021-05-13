from collections import Counter

H, W = map(int, input().split())
four, two, any = 0, 0, 0
if H % 2:
    if W % 2:
        two = H // 2 + W // 2
        any = 1
    else:
        two = W // 2
else:
    if W % 2:
        two = H // 2
four = (H * W - two * 2 - any) // 4
s = ''
for _ in range(H):
    s += str(input())
c = Counter(s)
d = {'four': 0, 'two': 0}
for v in c.values():
    d['four'] += v // 4
    v -= 4 * (v // 4)
    d['two'] += v // 2
if d['four'] >= four:
    d['two'] += (d['four'] - four) * 2
    if d['two'] == two:
        print('Yes')
    else:
        print('No')
else:
    print('No')

N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]

s = []
l = []
top = 2*(10**9)+1
low = 0
for j in range(N):
    t = sum(M[j])
    if low == t:
        s.append(M[j])
    elif low < t:
        low = t
        s = []
        s.append(M[j])

    if top == t:
        l.append(M[j])
    elif top > t:
        top = t
        l = []
        l.append(M[j])


def cal_man(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


s.sort()
l.sort()


high = []
small = []
lowest = 2*(10**9)+1
topest = -2*(10**9)+1
for j in range(N):
    t = M[j][1] - M[j][0]
    if lowest > t:
        lowest = t
        small = []
        small.append(M[j])
    elif lowest == t:
        small.append(M[j])

    if topest < t:
        topest = t
        high = []
        high.append(M[j])
    elif topest == t:
        high.append(M[j])
high.sort()
small.sort()


print(max([cal_man(s[0], l[-1]), cal_man(s[-1], l[0]),
           cal_man(high[0], small[-1]), cal_man(high[-1], small[0])]))

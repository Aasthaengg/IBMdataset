
def check(s):
    h = 0
    for p in s:
        b = h + p[0]
        if b < 0:
            return False
        h += p[1]
    return True


N = int(input())
S = []
left = []
right = []
total = 0
for i in range(N):
    last = 0
    bottom = 0
    s = input().strip()
    for c in s:
        if c == "(":
            last += 1
        else:
            last -= 1
        bottom = min(bottom, last)
    if last > 0:
        left.append((bottom, last))
    else:
        right.append((bottom-last, -last))
    total += last

left.sort(key=lambda x: -x[0])
right.sort(key=lambda x: -x[0])

if check(left) and check(right) and total == 0:
    print('Yes')
else:
    print('No')

n = int(input())
S = [input() for i in range(n)]
AB = []
for i in range(n):
    a, b = 0, 0
    for c in S[i]:
        if c == '(':
            b += 1
        if c == ')':
            if b > 0:
                b -= 1
            else:
                a += 1
    AB.append((a, b))
AB0 = [(a, b) for a, b in AB if -a + b >= 0]
AB1 = [(a, b) for a, b in AB if -a + b < 0]
AB0.sort()
AB1.sort(key=lambda x: -x[1])
AB = AB0 + AB1
x = 0
for a, b in AB:
    x -= a
    if x < 0:
        print('No')
        exit()
    x += b
if x == 0:
    print('Yes')
else:
    print('No')

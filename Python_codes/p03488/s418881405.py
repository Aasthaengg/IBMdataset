s = input().split('T')
X, Y = map(int, input().split())

x = [len(i) for i in s[0::2]]
y = [len(i) for i in s[1::2]]

X = X - x[0]

x, y = sorted(x[1:]), sorted(y)

while x:
    mx = x.pop()
    if X < 0:
        X += mx
    else:
        X -= mx

while y:
    my = y.pop()
    if Y < 0:
        Y += my
    else:
        Y -= my

print('Yes' if X == 0 and Y == 0 else 'No')

n = list(map(int, input().split()))
W = n[0]
H = n[1]
x = n[2]
y = n[3]
r = n[4]
if (x >= r and y >= r and (x + r) <= W and (y + r) <= H):
    print('Yes')
else:
    print('No')
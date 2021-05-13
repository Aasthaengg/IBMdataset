(W,H,x,y,r) = input().rstrip().split(' ')
W = int(W)
H = int(H)
x = int(x)
y = int(y)
r = int(r)

if x - r >= 0 and y - r >= 0 and x + r <= W and y + r<= H:
    print('Yes')
else:
    print('No')
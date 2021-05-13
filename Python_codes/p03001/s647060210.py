#ABC130 C-Rectangle Cutting 14:59

W,H,x,y = map(int, input().split())

def func(W,H,x,y):
    if x* 2 == W and y*2 == H:
        return W*H/2, 1
    else:
        return W*H/2, 0
print(*func(W,H,x,y))
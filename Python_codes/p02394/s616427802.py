from sys import stdin

W, H, x, y, r = [int(x) for x in stdin.readline().rstrip().split()]

def isInner(px, py):
    if( px < 0 or px > W ):
        return False
    else: # x座標は長方形の内部
        if( py < 0 or py > H ):
            return False
        else:
            return True

if( isInner(x-r, y) and isInner(x+r, y) and isInner(x, y-r) and isInner(x, y+r) ):
    print("Yes")
else:
    print("No")


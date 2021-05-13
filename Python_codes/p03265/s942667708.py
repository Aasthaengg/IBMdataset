def resolve():
    x1, y1, x2, y2 = list(map(int, input().split()))
    diff1 = y2-y1
    diff2 = x2-x1
    x3, y3 = x2 - diff1,  y2 + diff2
    x4, y4 = x1 - diff1,  y1 + diff2
    print(x3, y3, x4, y4)
        

if '__main__' == __name__:
    resolve()
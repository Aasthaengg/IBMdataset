li = list(map(int,input().split()))
rect_a = li[0]*li[1]
rect_b = li[2]*li[3]
if rect_a > rect_b:
    print(str(rect_a))
else:
    print(str(rect_b))
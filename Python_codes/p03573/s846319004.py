def dif_num(x,y):
    if x == y:
        return 0
    else:
        return 1

a,b,c = map(int,input().split())
if dif_num(a,b) == 1 and dif_num(a,c) == 1:
    print(a)
if dif_num(a,b) == 1 and dif_num(b,c) == 1:
    print(b)
if dif_num(a,c) == 1 and dif_num(c,b) == 1:
    print(c)
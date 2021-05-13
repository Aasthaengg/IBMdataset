A,B,C = (int(a) for a in input().split())
x = C - (A - B)
if x <= 0 :
    print(0)
else : print(x)
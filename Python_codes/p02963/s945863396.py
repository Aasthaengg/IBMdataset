import math
N = input()
l = len(N)
N =int(N)
a = b  =0
# def up(num):
    #100098,1 →110000
    #100098,2 → 101000
    #
MAX = 10 ** 9
for i in range(0,19):
    juu = 10 ** i
    dived = math.ceil(N / juu)
    # print(dived * juu)
    x1 = dived
    y2 = juu
    x2 = dived * juu - N
    y1 = 1

    # print(c,d,e,f)
    if MAX >= x1 >= 0 and MAX >= x2 >= 0 and MAX >= y1 >= 0 and MAX >= y2 >= 0 :
        print(a, b, x1, y1, x2,y2)
        exit(0)
    #






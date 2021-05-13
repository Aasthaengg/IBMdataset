a , b = map(int, input().split())
if b==1:
    print(0)
elif b <=a:
    print(1)
elif b > a and (b - 1)%(a - 1)== 0:
    print((b - 1)// (a - 1))
elif b > a and (b - 1)%(a - 1)!= 0:
    print((b - 1)//(a - 1)+ 1)
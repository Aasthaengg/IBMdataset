a,b = input().split()
a = int(a)
b = int(b)

if 0 <= a <= 100:
    if 2 <= b <= 1000 and (b%2 == 0):
        if a >= 13 :
            print(int(b))
        if 6 <= a <= 12:
            x = b/2
            print(int(x))
        if a <= 5 :
            print(int(0))
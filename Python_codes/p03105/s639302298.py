a,b,c = input().split()

a = int(a)
b = int(b)
c = int(c)

if 1 <= a <= 100:
    if 1 <= b <= 100:
        if 1<= c <= 100:

            x = b / a
            if x >= c:
                print(int(c))
            else:
                print(int(x))
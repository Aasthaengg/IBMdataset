def do():
    n = int(input())
    for b in range(1,3501):
        for c in range(1,3501):
            if (4*b*c - n*b - n*c) == 0:
                continue
            a = (n*b*c) / (4*b*c - n*b - n*c)
            if a < 1:
                continue
                

            if a.is_integer():
                print(int(a),b,c)
                return 0
    return 0
do()
def Euclid(max, min):
    if max % min == 0:
        return min
    else:
        return Euclid(min, max % min)


a, b = map(int, input().split(" "))
if a > b:
    print(Euclid(a, b))
else:
    print(Euclid(b, a))
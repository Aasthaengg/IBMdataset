x = list(input())
first = 10 * int(x[0]) + int(x[1])
second = 10 * int(x[2]) + int(x[3])


def mc(num):
    if 1 <= num <= 12:
        return True
    else:
        return False


def yc(num):
    if 0 <= num <= 99:
        return True
    else:
        return False


if yc(first):
    if mc(second):
        if yc(second):
            if mc(first):
                print("AMBIGUOUS")
            else:
                print("YYMM")
        else:
            print("YYMM")
    elif yc(second):
        if mc(first):
            print("MMYY")
        else:
            print("NA")
    else:
        print("NA")
elif yc(second):
    if mc(first):
        print("MMYY")
    else:
        print("NA")
else:
    print("NA")

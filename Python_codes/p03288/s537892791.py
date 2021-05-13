def resolve():
    R = int(input())
    if R < 1200:
        print("ABC")
    elif R < 2800:
        print("ARC")
    else:
        print("AGC")

if '__main__' == __name__:
    resolve()
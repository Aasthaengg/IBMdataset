
def resolve():
    A, B = input().split()
    print("H" if (A=="H" and B=="H") or (A=="D" and B=="D") else "D")


if '__main__' == __name__:
    resolve()
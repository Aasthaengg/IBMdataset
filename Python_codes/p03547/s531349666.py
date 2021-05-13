
def resolve():
    X, Y = input().split()
    if X == Y :
        print("=")
    elif X < Y:
        print("<")
    else:
        print(">")


if '__main__' == __name__:
    resolve()
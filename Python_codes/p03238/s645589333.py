def resolve():
    N = int(input())
    if N==1:
        print("Hello World")
        return
    A = int(input())
    B = int(input())
    print(A+B)


if '__main__' == __name__:
    resolve()
def resolve():
    N = int(input())
    A = int(input())
    print("Yes" if N % 500 <= A else "No")


if '__main__' == __name__:
    resolve()
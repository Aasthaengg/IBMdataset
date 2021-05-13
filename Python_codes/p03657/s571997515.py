
def resolve():
    A, B = list(map(int, input().split()))
    print("Possible" if A%3==0 or B%3==0 or (A+B)%3==0 else "Impossible")


if '__main__' == __name__:
    resolve()
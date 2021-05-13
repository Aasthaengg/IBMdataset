
def resolve():
    A, B = list(map(int, input().split()))
    print(A+B if A+B<10 else "error")
    


if '__main__' == __name__:
    resolve()
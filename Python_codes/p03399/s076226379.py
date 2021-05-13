def resolve():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    print(min([A, B])+min([C, D]))

if '__main__' == __name__:
    resolve()
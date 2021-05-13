def resolve():
    A, B, C = list(map(int, input().split()))
    print(min(C, B//A))

if '__main__' == __name__:
    resolve()
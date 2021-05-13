
def resolve():
    A, op, B = input().split()
    if op == "+":
        print(int(A)+int(B))
    else:
        print(int(A)-int(B))


if '__main__' == __name__:
    resolve()

def resolve():
    A, B, C = list(map(int, input().split()))
    print("Yes" if A<= C and C <= B else "No")
    


if '__main__' == __name__:
    resolve()
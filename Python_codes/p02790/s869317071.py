def resolve():
    a, b = list(map(int, input().split()))
    print(str(a)*b if a < b else str(b)*a)

if '__main__' == __name__:
    resolve()
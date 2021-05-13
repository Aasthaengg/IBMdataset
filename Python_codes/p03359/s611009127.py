def resolve():
    a, b = list(map(int, input().split(" ")))
    print(a if a <= b else a-1)

if '__main__' == __name__:
    resolve()
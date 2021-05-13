def resolve():
    a, b, c, d = list(map(int, input().split(" ")))
    if abs(c - a) <= d:
        print("Yes")
        return
    if abs(b - a) <= d and abs(c - b) <= d:
        print("Yes")
        return
    print("No")

if '__main__' == __name__:
    resolve()
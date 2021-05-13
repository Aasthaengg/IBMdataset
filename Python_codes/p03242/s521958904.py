def resolve():
    n = input()
    print(int(n.replace("1", "x").replace("9", "1").replace("x", "9")))

if '__main__' == __name__:
    resolve()
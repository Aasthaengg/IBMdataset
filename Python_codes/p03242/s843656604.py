def resolve():
    N = input()
    N = N.replace("9", "0")
    N = N.replace("1", "9")
    N = N.replace("0", "1")
    print(N)


resolve()

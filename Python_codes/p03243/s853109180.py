def resolve():
    N = input()
    a, b, c = list(N)
    if a < b or (a == b and a < c):
        a = int(a) + 1
    print(a, a, a, sep="")


resolve()

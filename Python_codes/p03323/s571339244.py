def resolve():
    A, B = list(map(int, input().split(" ")))
    if A < B:
        A, B = B, A
    res = (A - B) <= (16 - 2 * B) / 2
    print("Yay!" if res else ":(")    

if '__main__' == __name__:
    resolve()
def resolve():
    n = input()
    l = len(n)
    if n[1:] == "9" * (l-1): #c9999...99のとき
        print(int(n[0]) + 9*(l-1))
    else:
        print((int(n[0])-1) + (9*(l-1)))
resolve()
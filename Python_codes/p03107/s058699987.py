def resolve():
    inp = input()

    c0 = inp.count('0')
    c1 = inp.count('1')

    print(min(c0, c1)*2)

resolve()
def resolve():
    S = input()
    s0 = S.count("0")
    s1 = S.count("1")
    print(min(s0, s1) * 2)


resolve()

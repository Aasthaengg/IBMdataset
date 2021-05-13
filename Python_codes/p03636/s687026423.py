def resolve():
    S = input()
    cnt = len(S[1:-1])
    print("{}{}{}".format(S[0], cnt, S[-1]))


if '__main__' == __name__:
    resolve()
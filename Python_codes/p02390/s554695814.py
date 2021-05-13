if __name__ == '__main__':
    S = int(input())
    s, S = S%60, S//60
    m, S = S%60, S//60
    print("{0}:{1}:{2}".format(S, m, s))
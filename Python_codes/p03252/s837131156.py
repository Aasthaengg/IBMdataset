def main():
    S = input()
    T = input()
    d = dict()
    for s, t in zip(S, T):
        if s not in d.keys():
            if t in d.values():
                print('No')
                return
            d[s] = t
        else:
            if d[s] != t:
                print('No')
                return
    print('Yes')


if __name__ == '__main__':
    main()
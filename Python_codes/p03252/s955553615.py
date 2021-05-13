def main():
    dic1 = {}
    dic2 = {}
    S = list(input().rstrip())
    T = list(input().rstrip())
    for s, t in zip(S, T):
        if s not in dic1:
            dic1[s] = t
        elif dic1[s] != t:
            print('No')
            exit()
        if t not in dic2:
            dic2[t] = s
        elif dic2[t] != s:
            print('No')
            exit()
    print('Yes')


if __name__ == '__main__':
    main()

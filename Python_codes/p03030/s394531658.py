def main():
    N = int(input())
    s_dict = dict()

    for i in range(1, N + 1):
        S, P = input().split()
        if S in s_dict:
            s_dict[S].append((i, int(P)))
        else:
            s_dict[S] = [(i, int(P))]

    s_dict_keys = sorted(list(s_dict.keys()))

    for key in s_dict_keys:
        s_dict[key].sort(key=lambda x: x[1], reverse=True)
        for i, _ in s_dict[key]:
            print(i)


if __name__ == "__main__":
    main()

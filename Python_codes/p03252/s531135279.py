def main():
    from string import ascii_lowercase
    S = input()
    T = input()

    dic1 = {a: set() for a in ascii_lowercase}
    dic2 = {a: set() for a in ascii_lowercase}
    for s, t in zip(S, T):
        dic1[s].add(t)
        dic2[t].add(s)
    if all(len(s) <= 1 for s in dic1.values()) and\
            all(len(s) <= 1 for s in dic2.values()):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()

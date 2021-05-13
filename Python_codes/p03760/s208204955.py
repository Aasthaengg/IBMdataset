def main():
    O = input()
    E = input()
    last = ""
    if len(O) > len(E):
        last = O[-1]
        O = O[:-1]

    ans = ""
    for s1, s2 in zip(O, E):
        ans += s1 + s2

    ans += last
    print(ans)


if __name__ == "__main__":
    main()
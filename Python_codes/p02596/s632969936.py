def main():
    K = int(input())
    mod = 7 % K
    mods = set([mod])
    if mod == 0:
        print(1)
        exit()
    ans = 1
    while True:
        ans += 1
        mod = (mod * 10 + 7) % K
        if mod == 0:
            print(ans)
            exit()
        elif mod in mods:
            print(-1)
            exit()
        else:
            mods.add(mod)


if __name__ == '__main__':
    main()

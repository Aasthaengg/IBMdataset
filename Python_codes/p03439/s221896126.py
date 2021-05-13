def main():
    import sys
    input = sys.stdin.readline

    def ask(n):
        print(n)
        sys.stdout.flush()
        s = input().rstrip('\n')
        if s == 'Vacant':
            exit()
        elif s == 'Male':
            return 0
        else:
            return 1

    N = int(input())

    a0 = ask(0)
    ok = 0
    ng = N-1
    mid = ((ng//2)//2) * 2
    while ng - ok > 2:
        a = ask(mid)
        if a == a0:
            ok = mid
        else:
            ng = mid
        mid = (((ok//2)+(ng//2))//2)*2
    ask((ok+ng)//2)
    ask(N-1)


if __name__ == '__main__':
    main()

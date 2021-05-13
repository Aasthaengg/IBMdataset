def main():
    N = int(input())
    s = input()
    t = input()
    ss = tt = ''
    l = 0
    for i in range(N):
        ss = s[-1-i] + ss
        tt = tt + t[i]
        if ss == tt:
            l = len(ss)
    print(2 * N - l)
    return

if __name__ == '__main__':
    main()

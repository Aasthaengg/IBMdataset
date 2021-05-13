def main():
    #入力
    N, A, B, C, D = (int(_) for _ in input().split())
    A, B, C, D = A-1, B-1, C-1, D-1
    S = input()

    sa, sb = S[A:C+1], S[B:D+1]
    can1 = can2 = True
    for i in range(len(sa)-1):
        if sa[i] == '#' and sa[i+1] == '#': can1 = False
    for i in range(len(sb)-1):
        if sb[i] == '#' and sb[i+1] == '#': can2 = False
    can = can1 and can2

    if can and D < C:
        sc = S[B-1:D+2]
        can3 = False
        for i in range(len(sc)-2):
            if sc[i] == '.' and sc[i+1] == '.' and sc[i+2] == '.': can3 = True
        can = can and can3

    print('Yes' if can else 'No')
    return

if __name__ == '__main__':
    main()

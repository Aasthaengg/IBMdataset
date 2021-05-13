def main():
    N, A, B, C, D = list(map(int, input().split(' ')))
    S = input()
    if C == D:
        print('No')
    elif C < D:
        for s in [S[(A-1):C], S[(B-1):D]]:
            for i in range(len(s) - 1):
                if s[i:(i+2)] == '##':
                    print('No')
                    return
        print('Yes')
    else:
        # A B D C
        s = S[(A-1):C]
        for i in range(len(s) - 1):
            if s[i:(i + 2)] == '##':
                print('No')
                return
        s = S[(B-2):(D+1)]
        ok = False
        for i in range(1, len(s) - 1):
            if s[(i-1):(i+2)] == '...':
                ok = True
                break
        print('Yes' if ok else 'No')


if __name__ == '__main__':
    main()
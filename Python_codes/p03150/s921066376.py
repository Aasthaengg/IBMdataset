def main():
    S  = input()
    K = 'keyence'
    if len(S)<=7:
        if S == K:
            print('YES')
        else:
            print('NO')
    else :
        ShaveN = len(S) - 7
        for i in range(len(S) - ShaveN + 1):
            Shave = S[:i] + S[i+ShaveN:]
            if Shave == K:
                print('YES')
                return
        print('NO')


if __name__ == '__main__':
    main()

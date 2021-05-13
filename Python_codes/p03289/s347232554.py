def mi():
    return map(int, input().split())

def main():
    S = input()
    if S[0] != 'A':
        print('WA')
        return

    if S[2:-1].count('C') != 1:
        print('WA')
        return

    if S[0].replace('A', 'a')+S[1]+S[2:-1].replace('C', 'c')+S[-1:] != S.lower():
        print('WA')
        return

    print('AC')

if __name__ == '__main__':
    main()
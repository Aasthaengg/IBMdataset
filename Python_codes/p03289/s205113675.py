def resolve():
    S = str(input())
    if S[0] != 'A':
        print('WA')
        return

    if S[2:-1].count('C') != 1:
        print('WA')
        return

    if S.replace('A', 'a').replace('C', 'c') != S.lower():
        print('WA')
        return

    print('AC')

    return
resolve()
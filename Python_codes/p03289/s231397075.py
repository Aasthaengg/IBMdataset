def solve():
    S = input()
    cnt = 0
    if S[0] != 'A':
        print('WA')
        exit()
    for i in range(1, len(S)):
        if S[i].isupper():
            if i == 1 or i == len(S) - 1 or S[i] != 'C':
                print('WA')
                exit()
            cnt += 1
    if cnt != 1:
        print('WA')
        exit()
    print('AC')






if __name__ == "__main__":
    solve()
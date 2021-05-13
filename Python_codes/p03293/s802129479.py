def main():
    S = list(str(input()))
    T = list(str(input()))

    for i in range(len(S)):
        if S == T:
            print('Yes')
            return
        else:
            p = S.pop(-1)
            S.insert(0, p)
    print('No')
main()  
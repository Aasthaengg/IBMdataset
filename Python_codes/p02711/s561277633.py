def main():
    S = list(str(input()))
    N = len(S)
    for i in range(N):
        if S[i] == '7':
            print('Yes')
            return
    print('No')
main()

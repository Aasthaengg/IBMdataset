def main():
    N = int(input())
    S = str(input())
    if N % 2 == 1:
        print('No')
    elif N == 2:
        if S[0] == S[1]:
            print('Yes')
        else:
            print('No')
    else:
        n = (N // 2) - 1
        na = n + 1
        if S[0:n] == S[na:-1]:
            print('Yes')
        else:
            print('No')
main()
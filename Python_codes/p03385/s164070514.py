def main():
    S = list(str(input()))
    if S[0] != S[1] and S[1] != S[2] and S[0] != S[2]:
        print('Yes')
    else:
        print('No')
main()
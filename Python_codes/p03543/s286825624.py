def main():
    N = list(str(input()))
    if N[0] == N[1] == N[2] or N[1] == N[2] == N[3]:
        print('Yes')
    else:
        print('No')
main()
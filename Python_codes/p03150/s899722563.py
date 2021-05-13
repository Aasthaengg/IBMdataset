
def main():
    S = input()
    N = len(S)
    for i in range(N):
        for j in range(N-i):
            if S[:j] + S[j+i:] == 'keyence':
                print('YES')
                return
    print('NO')


if __name__ == "__main__":
    main()
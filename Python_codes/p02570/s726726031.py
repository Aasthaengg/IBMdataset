
def main(D, T, S):
    print('Yes' if D <= T * S else 'No')

if __name__ == '__main__':
    D, T, S = map(int, input().split())
    main(D, T, S)

def main():

    N, K = map(int, input().split())
    if K == 1: return 0

    return N-K



if __name__ == '__main__':
    print(main())

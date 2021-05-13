def main():
    X, Y, A, B, C = list(map(int, input().split(' ')))
    P = list(map(int, input().split(' ')))
    Q = list(map(int, input().split(' ')))
    R = list(map(int, input().split(' ')))
    P.sort(reverse=True)
    Q.sort(reverse=True)
    R = R + P[:X] + Q[:Y]
    R.sort(reverse=True)
    print(sum(R[:(X+Y)]))


if __name__ == '__main__':
    main()

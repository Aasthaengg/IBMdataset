def main():
    N = int(input())
    A = list(map(int, input().split(' ')))
    A.sort()
    max_a = A[-1]
    A = A[:-1]
    A.sort(key=lambda a: abs(a - max_a / 2))
    print('{} {}'.format(max_a, A[0]))


if __name__ == '__main__':
    main()

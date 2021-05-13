def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    plus = 0
    minus = 0
    for a, b in zip(A, B):
        if b - a > 0:
            plus += (b - a)//2
        else:
            minus += a - b
    if plus >= minus:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()

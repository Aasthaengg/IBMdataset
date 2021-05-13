def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    A = list(map(lambda x: x % 2, A))
    if sum(A) == 0:
        print('second')
    else:
        print('first')


main()

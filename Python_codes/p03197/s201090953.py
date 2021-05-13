def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    exist_odds = False
    for a in A:
        if a % 2 == 1:
            exist_odds = True
            break
    if exist_odds:
        print('first')
    else:
        print('second')


if __name__ == '__main__':
    main()
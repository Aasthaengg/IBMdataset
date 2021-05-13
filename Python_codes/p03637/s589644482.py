def main():
    N = int(input())
    A = list(map(int, input().split(' ')))
    c_4, c_2, c_0 = 0, 0, 0
    for a in A:
        if a % 4 == 0:
            c_4 += 1
        elif a % 2 == 0:
            c_2 += 1
        else:
            c_0 += 1
    if c_2 == N:
        print('Yes')
    elif 0 < c_2 < N:
        print('Yes' if c_4 > 0 and c_4 >= c_0 else 'No')
    else:
        print('Yes' if c_4 >= c_0 - 1 else 'No')


if __name__ == '__main__':
    main()
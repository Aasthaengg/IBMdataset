def main():
    N = int(input())
    A = list(map(int, input().split()))
    x1 = 0
    for i, a in enumerate(A):
        if i % 2 == 0:
            x1 += a
        else:
            x1 -= a
    x_list = [x1]
    for a in A[:-1]:
        x_list.append(2 * a - x_list[-1])
    print(' '.join([str(x) for x in x_list]))


if __name__ == '__main__':
    main()

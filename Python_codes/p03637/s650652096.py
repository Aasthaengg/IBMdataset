def main():
    N = int(input())
    A = list(map(int, input().split()))
    n_odd = 0
    n_4mul = 0
    n_2mul = 0
    for a in A:
        if a % 2 == 1:
            n_odd += 1
        elif a % 4 == 0:
            n_4mul += 1
        else:
            n_2mul += 1
    if n_odd == 0:
        print('Yes')
    elif n_odd <= n_4mul and n_2mul > 0:
        print('Yes')
    elif n_odd == n_4mul + 1 and n_2mul == 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()

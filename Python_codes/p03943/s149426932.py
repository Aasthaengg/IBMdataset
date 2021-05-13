def main():
    candy = [int(cn) for cn in input().split()]
    candy.sort()
    print('Yes' if candy[0] + candy[1] == candy[2] else 'No')


if __name__ == '__main__':
    main()

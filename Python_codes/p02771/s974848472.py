def main():
    a, b, c = (int(i) for i in input().rstrip().split(' '))
    print('No' if (a == b == c) or ((a != b) and (a != c) and (b != c)) else 'Yes')


if __name__ == '__main__':
    main()

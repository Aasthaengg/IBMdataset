def main():
    A, B = (int(i) for i in input().split())
    print(max(A - 2*B, 0))


if __name__ == '__main__':
    main()

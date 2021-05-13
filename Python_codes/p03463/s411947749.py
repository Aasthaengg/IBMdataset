def main():
    N, A, B = (int(i) for i in input().split())
    if (B - A) % 2:
        print("Borys")
    else:
        print("Alice")


if __name__ == '__main__':
    main()

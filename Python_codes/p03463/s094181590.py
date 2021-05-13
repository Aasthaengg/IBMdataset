def main():
    length, alice, borys = map(int, input().split())
    print("Alice" if (borys - alice) % 2 == 0 else "Borys")


if __name__ == '__main__':
    main()


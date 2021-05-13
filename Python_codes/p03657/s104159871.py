def main():
    a, b = map(int, input().split())
    print("Possible" if a * b * (a + b) % 3 == 0 else "Impossible")


if __name__ == '__main__':
    main()
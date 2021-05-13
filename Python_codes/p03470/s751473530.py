def main():
    N = int(input())
    diameters = [int(input()) for x in range(N)]
    unique = list(dict.fromkeys(diameters))
    print(len(unique))


if __name__ == '__main__':
    main()

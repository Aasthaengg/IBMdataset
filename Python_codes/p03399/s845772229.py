def main():
    fares = []
    for _ in range(4):
        fares.append(int(input()))
    print(min(fares[0], fares[1]) + min(fares[2], fares[3]))


if __name__ == '__main__':
    main()
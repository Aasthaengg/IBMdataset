def main():
    S = input()
    k = int(input())
    for s in S[:k]:
        if s != '1':
            print(s)
            break
    else:
        print(1)


if __name__ == '__main__':
    main()

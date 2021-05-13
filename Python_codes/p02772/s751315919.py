def main():
    N = input()
    A = [v for v in map(int, input().split()) if v % 2 == 0]
    for a in A:
        if a % 3 != 0 and a % 5 != 0:
            print("DENIED")
            exit()
    print("APPROVED")


if __name__ == '__main__':
    main()

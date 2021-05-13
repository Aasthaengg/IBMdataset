def main():
    n,k = map(int, input().split())

    if n%k != 0:
        print(1)
        return
    print(0)

if __name__ == '__main__':
    main()

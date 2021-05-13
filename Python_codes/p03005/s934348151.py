def main():
    n, k = list(map(int, input().split()))
    if k == 1:
        print(0)
    else:
        print(n - k)
if __name__ == '__main__':
    main()

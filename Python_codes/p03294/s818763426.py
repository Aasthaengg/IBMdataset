def main():
    n, *a = map(int, open(0).read().split())
    ans = sum(a) - n
    print(ans)

if __name__ == '__main__':
    main()

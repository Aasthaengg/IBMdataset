def main():
    N, K = (int(i) for i in input().split())
    L = [int(i) for i in input().split()]
    L.sort(reverse=True)
    print(sum(L[:K]))


if __name__ == '__main__':
    main()

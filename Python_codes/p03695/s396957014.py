def main():
    n = int(input())
    a = list(map(int, input().split()))
    l = [i//400 for i in a if i < 3200]
    c = len(set(l))
    print(max(1, c), c+n-len(l))


if __name__ == '__main__':
    main()

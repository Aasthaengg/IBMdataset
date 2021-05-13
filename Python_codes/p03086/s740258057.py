def main():
    # n = int(input())
    # n, m = map(int, input().split())
    # a = list(map(int, input().split()))
    s = input()
    # h = [int(input()) for _ in rane(n)]
    count = 0
    maxi = 0
    for string in s:
        if string == "A" or string == "C" or string == "G" or string == "T":
            count += 1
            maxi= max(count, maxi)
        else:
            count = 0

    print(maxi)


if __name__ == '__main__':
    main()

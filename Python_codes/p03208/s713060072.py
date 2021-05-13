def main():
    # n = int(input())
    n, m = map(int, input().split())
    # v = list(map(int, input().split()))
    # s = input()
    h = [int(input()) for _ in range(n)]

    h.sort()

    temp = []
    for i in range(n-m+1):
        temp.append(h[i+m-1]-h[i])

    temp.sort()
    print(temp[0])


if __name__ == '__main__':
    main()

def main():
    # n = int(input())
    n, q = map(int, input().split())
    # a = list(map(int, input().split()))
    s = input()
    # h = [int(input()) for _ in rane(n)]
    lr = []
    for i in range(q):
        l, r = list(map(int, input().split()))
        lr.append([l-1, r-1])

    count = [0] * (10**6)
    for i in range(1, n):
        if s[i-1] == "A" and s[i] == "C":
            count[i] = count[i-1] + 1
        else:
            count[i] = count[i-1]

    for i in range(q):
        print(count[lr[i][1]] - count[lr[i][0]])


if __name__ == '__main__':
    main()

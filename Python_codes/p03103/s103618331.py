def main():
    # n = int(input())
    n, m = map(int, input().split())
    # a = list(map(int, input().split()))
    # s = input()
    # h = [int(input()) for _ in rane(n)]

    ab = []
    for i in range(n):
        a, b = map(int, input().split())
        ab.append([a, b])

    cost = 0
    temp_i = 0
    ab.sort(key=lambda x: x[0])
    for i in range(n):
        cost += ab[i][0] * ab[i][1]
        m -= ab[i][1]
        if m <= 0:
            temp_i = i
            break

    if m == 0:
        print(cost)
    elif m < 0:
        cost += ab[temp_i][0] * m
        print(cost)


if __name__ == '__main__':
    main()

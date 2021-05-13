def main():
    # n = int(input())
    # n, m = map(int, input().split())
    # a = list(map(int, input().split()))
    # s = input()
    # h = [int(input()) for _ in rane(n)]

    import math

    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    dishes = [a, b, c, d, e]
    count = 0
    mini = 10
    index = 0
    for i in range(5):
        if dishes[i] % 10 != 0 and mini > dishes[i] % 10:
            mini = dishes[i] % 10
            index = i
    for i in range(5):
        if i != index:
            count += math.ceil(dishes[i]/10) * 10
        else:
            count += dishes[i]

    print(count)


if __name__ == '__main__':
    main()

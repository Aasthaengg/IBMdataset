def main():
    N = int(input())

    dict = {}
    total = 0
    for _ in range(N):
        s, t = input().split()
        total += int(t)
        dict[s] = total

    X = input()
    print(total-dict[X])


if __name__ == '__main__':
    main()
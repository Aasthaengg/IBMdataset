def main():
    N = int(input())
    info = [tuple(map(int, input().split())) for _ in range(N)]

    info.sort(key=lambda x: -(x[0]+x[1]))
    takahashi = sum([val for i, (val, _) in enumerate(info) if i % 2 == 0])
    aoki = sum([val for i, (_, val) in enumerate(info) if i % 2 == 1])
    print(takahashi-aoki)


if __name__ == "__main__":
    main()
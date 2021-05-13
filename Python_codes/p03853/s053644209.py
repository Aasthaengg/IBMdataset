def main():
    h, w = map(int, input().split())
    cs = [list(input()) for _ in range(h)]
    for i in range(h):
        print(*cs[i], sep="")
        print(*cs[i], sep="")


if __name__ == "__main__":
    main()

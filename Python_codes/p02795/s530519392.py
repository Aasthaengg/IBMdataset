def main():
    H = int(input())
    W = int(input())
    N = int(input())
    ans = -(-N//max(H, W))
    print(ans)


if __name__ == "__main__":
    main()

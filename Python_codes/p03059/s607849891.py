def main():
    A, B, T = map(int, input().split())
    ans = int(T / A) * B
    print(ans)


if __name__ == "__main__":
    main()

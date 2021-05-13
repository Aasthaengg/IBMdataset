def main():
    paints = list(map(int, input().split()))
    ans = len(set(paints))
    print(ans)


if __name__ == "__main__":
    main()

# keyence2019
def main():
    N = set(map(int, input().rstrip().split()))
    print("YES" if N == {1, 4, 7, 9} else "NO")


if __name__ == "__main__":
    main()
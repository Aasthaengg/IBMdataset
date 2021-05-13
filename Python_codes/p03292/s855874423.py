
def main():
    n = map(int, input().split())
    sorted_n = sorted(n)
    print((sorted_n[1] - sorted_n[0]) + (sorted_n[2] - sorted_n[1]))


if __name__ == "__main__":
    main()

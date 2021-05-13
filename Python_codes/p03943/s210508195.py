
def main():
    n = map(int, input().split())
    n_sorted = sorted(n)
    if n_sorted[0] + n_sorted[1] == n_sorted[2]:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()

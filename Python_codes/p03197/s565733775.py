# caddi2018D - Harlequin
def main():
    N, *A = map(int, open(0).read().split())
    flg = any(i & 1 for i in A)
    print("first" if flg else "second")


if __name__ == "__main__":
    main()
# caddi2018D - Harlequin
def main():
    N, *A = map(int, open(0).read().split())
    flg = all(i % 2 == 0 for i in A)
    print("second" if flg else "first")


if __name__ == "__main__":
    main()
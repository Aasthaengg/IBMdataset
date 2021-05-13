# ABC118A - B +/- A
def main():
    A, B = map(int, input().split())
    flg = B % A
    print(B - A if flg else A + B)


if __name__ == "__main__":
    main()
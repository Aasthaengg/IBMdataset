# caddi2018D - Harlequin
def main():
    N, *A = map(int, open(0).read().split())
    for i in A:
        if i % 2:
            print("first")
            return
    print("second")


if __name__ == "__main__":
    main()
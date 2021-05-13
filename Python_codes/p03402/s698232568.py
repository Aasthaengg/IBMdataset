def main():
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    h = 40
    w = 100
    print(h, w)
    for i in range(10):
        X = "#." * min(A, 50) + "##" * max(50-A, 0)
        A = max(A-50, 0)
        print(X)
        print("#" * 100)
    for i in range(10):
        X = ".#" * min(B, 50) + ".." * max(50-B, 0)
        B = max(B-50, 0)
        print("." * 100)
        print(X)


if __name__ == "__main__":
    main()

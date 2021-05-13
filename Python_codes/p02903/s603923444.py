def main():
    H, W, A, B = map(int, input().split())
    
    for i in range(H):
        if i < B:
            row = "0" * A + "1" * (W - A)
        else:
            row = "1" * A + "0" * (W - A)
        print(row)


if __name__ == "__main__":
    main()
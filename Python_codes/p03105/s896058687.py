def main():
    A, B, C = map(int, input().split())
    x, y = divmod(B, A)
    if x < C:
        print(x)
    else:
        print(C)
if __name__ == "__main__":
    main()
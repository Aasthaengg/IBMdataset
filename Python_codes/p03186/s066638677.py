def main():
    A, B, C = map(int, input().split())
    C = min(C, A+B+1)
    print(B+C)


if __name__ == "__main__":
    main()

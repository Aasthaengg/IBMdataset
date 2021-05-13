def main():
    A, B, C = map(int, input().split())
    print("YNeos"[(A+B < C)::2])


if __name__ == "__main__":
    main()

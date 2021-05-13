
def main():
    a, b, c = map(int, input().split())
    result = (c - (a - b))
    if result >= 0:
        print(result)
    else:
        print(0)


if __name__ == "__main__":
    main()

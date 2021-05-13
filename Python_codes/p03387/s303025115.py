def main():
    a, b, c = map(int, input().split())
    total = a + b + c
    sa =  max(a, b, c) * 3 - total

    if sa % 2 == 0:
        print(sa // 2)
    else:
        print(sa // 2 + 2)
        




if __name__ == "__main__":
    main()
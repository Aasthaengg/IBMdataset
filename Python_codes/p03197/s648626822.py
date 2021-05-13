def main():
    n = int(input())
    f = False
    for i in range(n):
        a = int(input())
        if a%2 == 1:
            f = True
    if f:
        print("first")
    else:
        print("second")

if __name__ == "__main__":
    main()

def main():
    a, b = input().split()
    a += b
    n = int(a)
    i = 1
    while i * i <= n:
        if i * i == n:
            print("Yes")
            exit()
        i += 1
    print("No")

if __name__ == "__main__":
    main()
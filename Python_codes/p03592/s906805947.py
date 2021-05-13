def main():
    n, m, k = map(int, input().split())
    f = False
    for i in range(n+1):
        for j in range(m+1):
            if i*j + (n-i)*(m-j) == k:
                f = True
    if f:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()

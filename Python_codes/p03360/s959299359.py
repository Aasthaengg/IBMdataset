def main():
    a = list(map(int, input().split()))
    k = int(input())
    a.sort()
    print(a[0]+a[1]+a[2]*(2**k))

if __name__ == "__main__":
    main()

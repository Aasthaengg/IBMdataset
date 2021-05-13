def main():
    k = int(input())
    a, b = map(int, input().split())
    f = [1 for i in range(a, b+1) if i%k == 0]
    if f:
        print("OK")
    else:
        print("NG")

if __name__ == "__main__":
    main()
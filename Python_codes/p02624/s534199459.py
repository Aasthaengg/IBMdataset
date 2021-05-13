def main():
    n = int(input())
    ans = 0
    for i in range(1,n+1):
        s = n//i * (1+n//i) * i/2
        ans += s
    print(int(ans))

if __name__ == "__main__":
    main()

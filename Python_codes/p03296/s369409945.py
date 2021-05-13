def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        if i < n-2 and a[i] == a[i+1] == a[i+2]:
            a[i+1] = -1
            ans += 1
        if a[i] == a[i+1]:
            a[i] = -1
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()
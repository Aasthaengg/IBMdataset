def main():
    s = list(input())
    k = int(input())
    n = len(s)
    for i in range(n):
        if s[i] != "1":
            ans = s[i]
            break
        if i == k-1:
            ans = s[i]
            break
        if i == n-1:
            ans = s[0]
    print(ans)


if __name__ == "__main__":
    main()

def main():
    s = input()
    a = [0]*26
    ans = 1
    cnt = 0
    for c in s:
        ans += cnt - a[ord(c) - ord("a")]
        a[ord(c) - ord("a")] += 1
        cnt += 1
    print(ans)

if __name__ == "__main__":
    main()
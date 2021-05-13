def main():
    s = input().rstrip()
    t = "CODEFESTIVAL2016"
    ans = 0
    for i in range(16):
        if s[i] != t[i]:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()

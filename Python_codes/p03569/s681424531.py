def main():
    s = input()
    l = 0
    r = len(s)-1
    ans = 0
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        elif s[l] == "x":
            l += 1
            ans += 1
        elif s[r] == "x":
            r -= 1
            ans += 1
        else:
            print(-1)
            exit()
    print(ans)
    return

if __name__ == '__main__':
    main()

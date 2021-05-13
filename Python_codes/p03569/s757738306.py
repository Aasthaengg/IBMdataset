import sys
input = sys.stdin.readline


def main():
    s = input().strip()
    l, r = 0, len(s)-1
    ans = 0
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        elif s[l] == "x" and s[r] != "x":
            ans += 1
            l += 1
        elif s[l] != "x" and s[r] == "x":
            ans += 1
            r -= 1
        else:
            print(-1)
            return
    print(ans)


if __name__ == '__main__':
    main()

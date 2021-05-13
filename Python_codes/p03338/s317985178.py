def main():
    input()
    s = input()
    ans = []
    for i in range(1, len(s)):
        left = set(s[:i])
        right = set(s[i:])
        ans.append(len(left & right))
    print(max(ans))


if __name__ == '__main__':
    main()
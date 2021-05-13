
def main():
    n, k = map(int, input().split())
    s = input()
    result = ''
    for i in range(0, len(s)):
        if i == k-1:
            result += s[i].lower()
        else:
            result += s[i]
    print(result)


if __name__ == "__main__":
    main()

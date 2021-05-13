def main():
    s = input().rstrip()
    k = int(input())
    for i in range(len(s)):
        x = ord("z") - ord(s[i]) + 1
        if k >= x and x != 26:
            k -= x
            s = s[:i] + "a" + s[i+1:]
        if i == len(s)-1:
            s = s[:i] + (chr(ord(s[i]) + (k%26)))
    print(s)

if __name__ == "__main__":
    main()

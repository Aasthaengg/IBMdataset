def main():
    s = input()
    t = input()
    c = 0
    for i in range(len(s)):
        if s[i] == t[i]:
            c += 1
    return c

if __name__ == "__main__":
    print(main())
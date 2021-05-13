

def main():
    s = input()
    ans = 0
    i = 0
    prev = ''
    while i < len(s):
        c = s[i]
        if c == prev:
            i += 1
            if i == len(s):
                break
            c += s[i]
        prev = c
        i += 1
        ans += 1
    print(ans)

if __name__ == "__main__":
    main()
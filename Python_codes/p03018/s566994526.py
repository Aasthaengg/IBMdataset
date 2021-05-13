def main():

    s = list(input())
    ans = 0
    h = 0
    i = 0
    while i < len(s):
        if s[i] == "A":
            h += 1
            # print(i, h, s)
            if s[i:i+3] == ["A", "B", "C"]:
                ans += h
                h -= 1
                i += 2
                s[i] = "A"
            else:
                i += 1
        else:
            h = 0
            i += 1
    return ans

if __name__ == '__main__':
    print(main())
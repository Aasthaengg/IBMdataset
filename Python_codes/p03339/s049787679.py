def main():
    n = int(input())
    s = input()

    wnum = s.count("W")
    enum = s.count('E')

    first = enum
    ans = first

    for i in range(n):
        if s[i] == "E":
            first -= 1
        if i >= 1:
            if s[i-1] == "W":
                first += 1
        if ans > first:
            ans = first
        #print(i, ans, first)
    print(ans)




if __name__ == "__main__":
    main()
def main():
    s = input().rstrip()
    t = "AKIHABARA"
    i = 0
    while i < len(t) and i < len(s):
        if s[i] != t[i]:
            if t[i] != "A":
                break
            t = t[:i] + t[i+1:]
            i -= 1
        i += 1
    if s == t or s+"A" == t:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()

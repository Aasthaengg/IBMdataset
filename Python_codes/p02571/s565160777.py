def main():
    s, t = input(), input()
    ans = len(t)
    for i in range(len(s) - len(t)+1):
        substr = s[i:i+len(t)]
        diff = 0
        for a, b in zip(substr, t):
            if a != b:
                diff += 1
        if ans > diff:
            ans = diff
    print(ans)

if __name__=="__main__":
    main()
def main():
    s = input()
    s = s.replace('BC', 'D')
    a = 0; d = 0
    ans = 0
    for t in s:
        if a > 0:
            if t == 'D':
                d += 1
            elif t == 'A':
                if d > 0:
                    ans += a*d
                    d = 0
            elif t != 'D' and d > 0:
                ans += a*d
                a = 0
                d = 0
            else:
                a = 0
                d = 0
        a += (t == 'A')
    if a > 0 and d > 0:
        ans += a*d
    print(ans)

if __name__ == "__main__":
    main()

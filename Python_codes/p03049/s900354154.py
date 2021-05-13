def main():
    N = int(input())
    A = [input() for i in range(N)]
    ans = 0
    ba = 0
    b = 0
    a = 0
    for s in A:
        ans += s.count("AB")
        if s[0] == "B" and s[-1] == "A":
            ba += 1
        elif s[0] == "B":
            b += 1
        elif s[-1] == "A":
            a += 1
    ans += (ba - 1 if ba > 1 else 0)
    if ba > 0 and a > 0 and b > 0:
        b += 1
        a += 1
        ans += min(a, b)
    elif ba > 0 and a == 0 and b == 0:
        pass
    elif ba > 0 and a > 0:
        ans += 1
    elif ba > 0 and b > 0:
        ans += 1
    elif ba == 0:
        ans += min(a, b)
    print(ans)


if __name__ == '__main__':
    main()

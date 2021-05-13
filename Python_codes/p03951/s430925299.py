def main():
    N = int(input())
    s = input()
    t = input()

    ans = 2 * N
    for i in range(N):
        s_ = s[i:]
        t_ = t[:len(t) - i]

        if s_ == t_:
            tmp = s + t[len(t) - i:]
            ans = min(ans, len(tmp))

    print(ans)

if __name__ == "__main__":
    main()
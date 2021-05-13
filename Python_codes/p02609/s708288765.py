def main():
    N = int(input())
    X = input()
    t = X.count("1")
    x1, x2 = int(X, 2) % (t-1) if t != 1 else 0, int(X, 2) % (t+1)
    for i in range(N):
        ans = 0
        if X[i] == "0":
            # 反転してt += 1
            x = x2 + pow(2, N-i-1, t+1)
            x %= t+1
            ans += 1
            while x > 0:
                b = "{:0b}".format(x).count("1")
                x %= b
                ans += 1
        elif X[i] == "1" and t != 1:
            # 反転してt -= 1
            x = x1 - pow(2, N-i-1, t-1)
            x %= t-1
            ans += 1
            while x > 0:
                b = "{:0b}".format(x).count("1")
                x %= b
                ans += 1
        else:
            # X[i] == "1" and t == 1
            ans = 0
        print(ans)


if __name__ == '__main__':
    main()

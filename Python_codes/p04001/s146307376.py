def main():
    s = input()
    f = s[0]
    n = len(s) - 1
    ans = 0
    
    for i in range(2 ** (n)):
        res = [0] * (n)
        for j in range(n):
            if (i >> j) & 1:
                res[j] = 1
                f += '+'
            f += s[j+1]
        ans += sum(map(int, f.split("+")))
        # print(f)
        # print('b', res)
        f = s[0]
    print(ans)

if __name__ == '__main__':
    main()
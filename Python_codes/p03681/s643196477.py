def main():
    n, m = list(map(int, input().split()))
    mod = 1000000007
    def factorial(num, mod):
        ans = 1
        if num <= 1: return ans
        for i in range(2, num + 1):
            ans = (ans * i) % mod
        return ans

    if abs(n - m) >= 2:
        print(0)
    elif abs(n - m) == 1:
        print(factorial(n, mod) * factorial(m, mod) % mod)
    else:
        print(2 * factorial(n, mod) * factorial(m, mod) % mod)




if __name__ == '__main__':
    main()

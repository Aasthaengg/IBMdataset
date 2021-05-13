def main():
    n, k = map(int, input().split())
    s = input()

    かわいそうな人たち = s.count('LR') + s.count('RL')
    t = min(かわいそうな人たち, k)
    u = n - (かわいそうな人たち + 1) + 2 * t
    print(min(n - 1, u))


if __name__ == '__main__':
    main()

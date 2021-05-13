if __name__ == '__main__':
    n = int(input())
    s = input()
    b = s.count('#')
    w = s.count('.')
    bb = 0
    ans = w
    for i in range(n):
        if s[i] == '#':
            bb += 1
        ww = n - (i + 1) - (b - bb)
        ans = min(ans, bb + ww)
    print(ans)

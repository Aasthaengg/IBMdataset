def solve():
    s = int(input())
    n = s
    a = {s}
    for i in range(2, 10 ** 6 + 1):
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        if n in a:
            print(i)
            exit()
        else:
            a.add(n)







if __name__ == '__main__':
    solve()

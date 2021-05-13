def solve():
    d = [int(input()) for _ in range(5)]
    d.sort(reverse=True, key=lambda a: a % 10 if a % 10 > 0 else 9)
    for i in range(4):
        d[i] = -(-d[i]//10) * 10
    print(sum(d))


if __name__ == '__main__':
    solve()

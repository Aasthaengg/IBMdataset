def solve():
    s = input()
    t = input()
    count = 0
    for i, j in zip(s, t):
        if i == j:
            count += 1
    print(count)


if __name__ == '__main__':
    solve()

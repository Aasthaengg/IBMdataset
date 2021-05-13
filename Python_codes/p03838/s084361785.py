def main():
    x, y = (int(i) for i in input().split())
    ans = 0
    if abs(x) == abs(y):
        if x*y < 0:
            ans += 1
    elif abs(x) < abs(y):
        if x == 0 and y > 0:
            ans += y
        elif x == 0 and y < 0:
            ans += abs(y) + 1
        elif x < 0 and y > 0:
            # -10 20
            ans += 1
            x = -x
            ans += y - x
        elif x > 0 and y < 0:
            # 3 -5
            ans += abs(y) - x + 1
        elif x < 0 and y < 0:
            # -10 -20
            ans += abs(y - x) + 2
        else:
            # 10 20
            ans += y - x
    elif abs(x) > abs(y):
        if x < 0 and y == 0:
            ans += abs(x)
        elif x > 0 and y == 0:
            ans += x + 1
        elif x < 0 and y > 0:
            # -20 10
            ans += abs(x) - y + 1
        elif x > 0 and y < 0:
            # 5 -3
            ans += 1
            y = -y
            ans += x - y
        elif x < 0 and y < 0:
            # -20 -10
            ans += abs(x - y)
        else:
            # 20 10
            ans += x - y + 2
    print(ans)


if __name__ == '__main__':
    main()

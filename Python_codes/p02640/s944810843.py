def Qb():
    ans = 'No'
    x, y = map(int, input().split())
    for b in range(0, x + 1):
        z = y - (4 * b)
        if z % 2 == 0 and x == (z / 2 + b):
            ans = 'Yes'
            break
    print(ans)


if __name__ == "__main__":
    Qb()

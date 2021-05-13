

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n, a, b = map(int, input().split())

    ans = 0
    for n in range(n + 1):
        keta = len(str(n))
        wa = 0
        for m in range(keta):
            tmp = str(n)
            wa = wa + int(tmp[-m-1])
        if a <= wa <= b:
            ans = ans + n

    print(ans)

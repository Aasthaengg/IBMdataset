

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    x = int(input())

    ans = 0

    for n in range(a + 1):
        for m in range(b + 1):
            for l in range(c + 1):
                if (500 * n + 100 * m + 50 * l) == x:
                    ans = ans + 1

    print(ans)


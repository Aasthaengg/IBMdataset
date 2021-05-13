def divisor(n):
    i = 1
    table = []
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table


def main():
    a, b = map(int, input().split())
    b_divide = divisor(b)
    if a in b_divide:
        ans = a + b
    else:
        ans = b - a
    print(ans)


if __name__ == "__main__":
    main()

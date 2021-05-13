def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


def main():
    a = int(input())
    a_dict = {a: 1}

    for i in range(2, 1000001):
        a = f(a)
        if a not in a_dict:
            a_dict[a] = 1
        else:
            print(i)
            break


if __name__ == "__main__":
    main()

def main(a, b):
    add = a + b
    sub = a - b
    mul = a * b

    return max(add, sub, mul)


if __name__ == "__main__":
    a, b = map(int, input().split(' '))
    print(main(a, b))

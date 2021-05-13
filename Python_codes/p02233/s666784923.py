def fibonacci(n):
    num1 = 1
    num2 = 1
    tmp = 1

    for i in range(1, n):
        tmp = num1 + num2
        num1 = num2
        num2 = tmp

    return tmp


if __name__ == '__main__':
    n = int(input())
    result = fibonacci(n)
    print(result)
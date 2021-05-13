def fibonacci(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b

    return b

if __name__ == '__main__':
    n = int(input())
    print(fibonacci(n))
def resolve():
    from math import sqrt
    
    n = int("".join(input().split()))
    print("Yes" if n == int(sqrt(n)) ** 2 else "No")


if __name__ == '__main__':
    resolve()
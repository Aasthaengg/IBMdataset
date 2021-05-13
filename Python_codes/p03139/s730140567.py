def resolve():
    n, a, b = map(int, input().split())
    if n >= a + b:
        mn = 0
    else:
        mn = a + b - n
    print(min(a, b), mn)

if __name__ == "__main__":
    resolve()

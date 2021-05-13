def f(x):
    return x * (x + 1) // 2


if __name__ == "__main__":
    N = int(input())
    for i in range(0, N + 1):
        if f(i) >= N:
            x, sum_ = i, f(i)
            break

    r = sum_ - N
    for i in range(1, x + 1):
        if i != r:
            print(i)

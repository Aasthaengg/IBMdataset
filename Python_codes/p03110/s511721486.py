def mi():
    return map(int, input().split())

def main():
    N = int(input())
    s = 0
    for _ in range(N):
        x, u = input().split()
        x = float(x)*(1 if u == 'JPY' else 380000.0)
        s += x

    print(s)


if __name__ == '__main__':
    main()
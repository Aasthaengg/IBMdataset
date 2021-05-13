#!python3

# input
N = int(input())
X = input()


def popcount(n):
    return bin(n).count("1")


def solve(n):
    if n == 0:
        return 0
    c = popcount(n)
    return 1 + solve(n % c)


def main():
    c = X.count("1")
    if c == 0:
        for _ in range(N):
            print(1)
        return
    a, b = 0, 0
    for i in range(N):
        if c == 1 and X[-1 - i] == "1":
            b = (b + pow(2, i, c + 1)) % (c + 1)
        elif X[-1 - i] == "1":
            a = (a + pow(2, i, c - 1)) % (c - 1)
            b = (b + pow(2, i, c + 1)) % (c + 1)
    for i in range(N):
        if c == 1 and X[i] == "1":
            print(0)
            continue
        if X[i] == "1":
            m = c - 1
            w = (a - pow(2, N - 1 - i, m)) % m
        else:
            m = c + 1
            w = (b + pow(2, N - 1 - i, m)) % m
        ans = solve(w) + 1
        print(ans)
            

if __name__ == "__main__":
    main()

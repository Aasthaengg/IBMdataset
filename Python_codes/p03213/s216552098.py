import math

def decompose(d, n):
    limit = (int)(math.sqrt(n)) + 1
    for i in range(2, limit):
        while n % i == 0:
            if i not in d:
                d[i] = 0
            d[i] += 1
            n //= i
    if n != 1:
        if n not in d:
            d[n] = 0
        d[n] += 1

def main():
    N = int(input())
    D = {}
    for i in range(2, N + 1):
        decompose(D, i)
    f2, f4, f14, f24, f74 = 0, 0, 0, 0, 0
    for d in D:
        n = D[d]
        if n >= 74:
            f74 += 1
        if n >= 24:
            f24 += 1
        if n >= 14:
            f14 += 1
        if n >= 4:
            f4 += 1
        if n >= 2:
            f2 += 1
    # print(D, f2, f4, f14, f24, f74)
    if f2 == 0 or f4 < 2:
        print(0)
        return
    # 75
    ans = f74
    # 25 * 3
    ans += f24 * (f2 - 1)
    # 15 * 5
    ans += f14 * (f4 - 1)
    # 5 * 5 * 3
    ans += f4 * (f4 - 1) // 2 * (f2 - 2)
    print(ans)

if __name__ == '__main__':
    main()

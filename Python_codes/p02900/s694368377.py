import math


def main():
    a, b = map(int, input().split())
    gcd = math.gcd(a, b)
    ans = [1]
    while gcd % 2 == 0:
        ans.append(2)
        gcd = gcd // 2
    f = 3
    while f * f <= gcd:
        if gcd % f == 0:
            ans.append(f)
            gcd = gcd // f
        else:
            f += 2
    if gcd != 1:
        ans.append(gcd)
    print(len(set(ans)))


if __name__ == '__main__':
    main()

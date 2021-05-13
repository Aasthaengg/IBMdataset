from fractions import gcd  # if python3.5~, use math.gcd


def f(x, a):
    return sum([x % aa for aa in a])


def main():
    N = int(input())
    a = list(map(int, input().split(' ')))
    gcd_a = a[0]
    for i in range(1, N):
        gcd_a = gcd(gcd_a, a[i])
    lcm_a = a[0]
    for i in range(1, N):
        lcm_a *= a[i] // gcd_a
    print(f(lcm_a - 1, a))


if __name__ == '__main__':
    main()

import math

def main():
    N = int(input())
    A = list(map(int, input().split()))
    lcm = 1
    for a in A:
        lcm = lcm * a // math.gcd(lcm, a)
    m = lcm - 1

    f = 0
    for a in A:
        f += m % a
    print(f)


if __name__ == '__main__':
    main()

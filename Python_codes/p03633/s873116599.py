import math

def main():
    N = int(input())
    T = [int(input()) for _ in range(N)]
    lcm = 1
    for t in T:
        lcm = lcm * t // math.gcd(lcm, t)
    print(lcm)


if __name__ == '__main__':
    main()

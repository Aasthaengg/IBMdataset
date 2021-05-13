from fractions import gcd
def main():
    n, m = list(map(int, input().split()))
    s = list(input())
    t = list(input())
    lcm = n * m // gcd(n, m)
    a, b = lcm // n, lcm // m
    lcmx = a * b // gcd(a, b)
    for i in range(lcm // lcmx):
        if s[i * b] != t[i * a]:
            print(-1)
            break
    else:
        print(lcm)

if __name__ == '__main__':
    main()

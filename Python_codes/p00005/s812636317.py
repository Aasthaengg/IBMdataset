def main():
    gcd = lambda n, m : gcd(m, n % m) if m != 0 else n
    while True:
        try:
            n, m = map(int, input().split())

            g = gcd(n, m)
            l = n * m // g

            print(g, l)
        except:
            break

if __name__ == '__main__':
    main()
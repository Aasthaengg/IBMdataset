import sys
def main():
    for line in sys.stdin:
        a,b = map(int, line.split())
        if a > b:
            a,b = b,a
        p = a * b #product

        while True:
            hoge = a
            a = b % a
            b = hoge
            if a == 0:
                gcd = b
                break

        lcm = p // gcd
        print(gcd, lcm)




if __name__ == "__main__":
    main()
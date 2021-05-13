from math import gcd
def main():
    a, b, c, d = map(int, input().split())
    ans = b - a + 1
    e = c*d // gcd(c, d)
    x = b//c - (a-1)//c
    y = b//d - (a-1)//d
    z = b//e - (a-1)//e
    print(ans - x - y + z)

if __name__ == "__main__":
    main()
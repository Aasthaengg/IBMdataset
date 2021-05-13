import fractions as math

def main():
    x, y = map(int, input().split())
    print(x*y // math.gcd(x,y))

if __name__ == '__main__':
    main()
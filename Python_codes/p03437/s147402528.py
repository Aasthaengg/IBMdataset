import sys
input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def main():
    x, y = map(int, input().split())

    if x < x * (y//gcd(x, y)):
        print(x)
    else:
        print(-1)
    


if __name__ == "__main__":
    main()
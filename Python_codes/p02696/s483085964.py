from math import floor
def main():
    a, b, n= map(int, input().split())
    x = min(n, b - 1)
    r = floor((a * x) / b) - a * floor(x / b)
    print(r)

if __name__ == '__main__':
    main()

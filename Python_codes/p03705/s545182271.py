def main():
    n, a, b = map(int, input().split())
    print(0 if (n == 1 and a != b) or a > b else (b - a) * (n - 1) + a - b + 1)
    
if __name__ == '__main__':
    main()

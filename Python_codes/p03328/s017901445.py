def main():
    a, b = map(int, input().split())
    c = b - a
    x = (1 + c) * c // 2
    print(x - b)
main()

def main():
    a, b = map(int, input().split())
    n = (b - a) - 1
    a_ = n*(n+1)/2
    print(int(a_ - a))
main()
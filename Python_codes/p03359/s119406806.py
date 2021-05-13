def main():
    a, b = map(int, input().split())
    if a == b:
        print(a)
    elif b > a:
        print(a)
    else:
        print(a - 1)
main()